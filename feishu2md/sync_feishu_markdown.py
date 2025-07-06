import os
import json
import subprocess
import filecmp
import shutil
from subprocess import Popen, PIPE

def runProcess(command):
    # 启动进程
    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    # feishu2md config --appId <your_id> --appSecret <your_secret>

    # 实时读取输出
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())

    # 等待完成并获取返回码
    return_code = process.wait()
    return return_code

def build_front_matter(document_info):
        return f"""---
title: "{document_info['title']}"
date: {document_info['date']}
categories: {document_info['categories']}
tags: {document_info['tags']}
---

"""

def sync_markdown_file(document_token, document_info):
    ## set path and var
    filename = f"{document_info['date'].split(' ')[0]}-{document_token}.md"
    # os.rename(f"feishu2md/{document_token}.md", f"feishu2md/{filename}")
    upgrade_markdown_headings(f"{document_token}.md") # 升级markdown标题
    os.rename(f"{document_token}.md", f"{filename}") # feishu2md下载在根目录

    target_path = os.path.join("_posts", filename)
    # md_path = os.path.join("feishu2md", filename)
    md_path = os.path.join("", filename)# feishu2md下载在根目录
    front_matter = build_front_matter(document_info)

    ## read source file content
    with open(md_path, "r", encoding="utf-8") as f:
        body = f.read().lstrip()

    ## add front matter
    if not front_matter.strip().endswith("\n"):
        front_matter += "\n"
    new_content = front_matter + "\n" + body

    ## read old file
    if os.path.exists(target_path):
        with open(target_path, "r", encoding="utf-8") as f:
            old_content = f.read()
        if old_content.strip() == new_content.strip():
            print(f"✅ No change in: {filename}")
            return  # Step 4：无变化，结束
        else:
            print(f"🔁 Change detected in: {filename}")
    else:
        print(f"🆕 New file: {filename}")

    ## overwrite the target file
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    ## git commit and push
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
    subprocess.run(["git", "add", target_path], check=True)
    subprocess.run(["git", "commit", "-m", f"🔄 sync: {filename}"], check=True)
    subprocess.run(["git", "push"], check=True)
    print(f"✅ Synced and pushed: {filename}")

def sync_static_file():
    # 1. 添加 static 目录变更到暂存区
    subprocess.run(["git", "add", "static"], check=True)

    # 2. 检查是否有暂存区变更（--quiet: 无变化则退出码为 0）
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])

    if result.returncode == 0:
        print("✅ static 目录无改动，无需提交。")
        return

    # 3. 配置 Git 用户信息（仅 GitHub Actions 必需）
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)

    # 4. commit + push
    subprocess.run(["git", "commit", "-m", "📦 sync: 更新 static 目录内容"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("✅ static 目录已提交并推送。")


def feishu2md(appId, appSecret, file_path):
    # Read Document Info
    ## check file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文档信息文件不存在: {file_path}")
    ## open file
    with open(file_path, 'r', encoding = 'utf-8') as f:
        Document_Info = json.load(f)


    # Download Markdown File
    ## set config
    setConfigCommand = ["feishu2md/feishu2md", "config", "--appId", appId, "--appSecret", appSecret]
    runProcess(setConfigCommand)

    ## download every md file
    for document_token, document_info in Document_Info.items():
        url = f"https://g8s2ogdg6r.feishu.cn/docx/{document_token}"
        downloadCommand = ["feishu2md/feishu2md", "dl", url]
        runProcess(downloadCommand)
        sync_markdown_file(document_token, document_info )
    sync_static_file()

def upgrade_markdown_headings(file_path: str) -> None:
    """
    Upgrades all Markdown headings in a file by one level.

    This function reads a Markdown file, identifies all the headings (e.g., #, ##),
    and adds an additional '#' to each, effectively demoting them by one level
    (e.g., H1 -> H2, H2 -> H3).

    Reason:
    - Chirpy only renders h2~h6 for body Markdown, not h1
    - Personal Reason: The headings in the documents I write all start from h1

    Key Features:
    - Ignores content within fenced code blocks (```) to prevent changing code.
    - Preserves original formatting, including blank lines and indentation.
    - Modifies the file in-place.
    - Defines a heading as one or more '#' characters followed by a space.

    Args:
        file_path (str): The path to the Markdown file to be modified.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return

    try:
        # Read all lines from the file, preserving line breaks
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    new_lines = []
    in_code_block = False

    for line in lines:
        stripped_line = line.strip()

        # Toggle the state if a code block fence is found
        if stripped_line.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue

        # If we are not in a code block, check for and process headings
        if not in_code_block:
            lstripped_line = line.lstrip()
            # Check if the line looks like a heading
            if lstripped_line.startswith('#'):
                # A valid heading must have a space after the hash marks.
                # This prevents treating things like '#include' or '#define' as headings.
                i = 0
                while i < len(lstripped_line) and lstripped_line[i] == '#':
                    i += 1
                
                # Condition for a valid heading: has '#'s and a space follows them.
                if i > 0 and i < len(lstripped_line) and lstripped_line[i] == ' ':
                    # It's a heading, so we upgrade it by one level.
                    # We must preserve the original indentation.
                    indent_len = len(line) - len(lstripped_line)
                    indent = line[:indent_len]
                    modified_line = indent + '#' + lstripped_line
                    new_lines.append(modified_line)
                else:
                    # It's not a valid heading, so leave it unchanged.
                    new_lines.append(line)
            else:
                # The line does not start with '#', so it's not a heading.
                new_lines.append(line)
        else:
            # We are inside a code block, so append the line without changes.
            new_lines.append(line)

    try:
        # Write the modified lines back to the original file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    appId = os.environ.get('appId')
    appSecret = os.environ.get('appSecret')
    file_path = 'feishu2md/Document_Info.json'
    feishu2md(appId, appSecret, file_path)
    
