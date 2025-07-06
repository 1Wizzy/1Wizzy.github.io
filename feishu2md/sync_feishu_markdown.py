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

if __name__ == "__main__":
    appId = os.environ.get('appId')
    appSecret = os.environ.get('appSecret')
    file_path = 'feishu2md/Document_Info.json'
    feishu2md(appId, appSecret, file_path)
    
