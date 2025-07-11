---
title: "记一个Github Bug"
date: 2025-07-12 00:03
categories: ['Blog']
tags: ['Blog', 'BUG']
---



## 记一个 Github Bug

> 在任何目录层级下，都不能有名字完全相同的两个文件夹或文件。

这个命题，相信小学二年级的同学都会认为它是对的，事实上它确实是对的。

但是，如下图

![](static/A6zvbaQSEoiNbCxjZpAcZIW9nNd.png)

有人说，是不是这三个文件夹存在一些不可见的字符呢？

![](static/ZPv3bk1JxoAenXxpcRMcDZu4nng.png)

确实，第三个显而易见的有个空白字符 `ᅟᅠ`。

但是，第一个和第二个究竟是什么情况 😨

接下来，打开这两个文件夹仔细观看：

![](static/B5uEbO4sRo6Im4xJr50c25uenOe.png)
![](static/CLSubfv0AofjLUxTGrrcFe1pnDe.png)

从 GitHub 选中的文件路径上来看，这两个路径几乎是一模一样的，难道命题是错的？

其实，从两个图片中的 `url` 中可以分析到：其实有一张图片中的文件夹名称后面多了一个 ` ` aka `%20`。

但是 Github 似乎不会渲染出来这个空格。

这个 B Bug 真的给我干无语了 😭

debug 过程中突然又想在本地 debug，遂直接 `git clone`，然后直接发现了问题

```bash
Wizzy@Wizzy-R7000P MINGW64 ~/Desktop/WorkingSpace
$ git clone https://github.com/1Wizzy/1Wizzy.github.io.git
Cloning into '1Wizzy.github.io'...
remote: Enumerating objects: 673, done.
remote: Counting objects: 100% (102/102), done.
remote: Compressing objects: 100% (65/65), done.
remote: Total 673 (delta 72), reused 37 (delta 36), pack-reused 571 (from 1)
Receiving objects: 100% (673/673), 46.42 MiB | 15.05 MiB/s, done.
Resolving deltas: 100% (230/230), done.
error: invalid path '_data/locales /en.yml'
fatal: unable to checkout working tree
warning: Clone succeeded, but checkout failed.
You can inspect what was checked out with 'git status'
and retry with 'git restore --source=HEAD :/'
```

显然由此得知，在 Windows 的文件系统不允许目录名以空格结尾 ❎

但是在 Linux/Unix 上，是完全没有问题的 ✅

```bash
root@Wizzy-R7000P:~# git clone https://github.com/1Wizzy/1Wizzy.github.io.git
Cloning into '1Wizzy.github.io'...
remote: Enumerating objects: 680, done.
remote: Counting objects: 100% (109/109), done.
remote: Compressing objects: 100% (71/71), done.
remote: Total 680 (delta 76), reused 37 (delta 36), pack-reused 571 (from 1)
Receiving objects: 100% (680/680), 46.42 MiB | 15.03 MiB/s, done.
Resolving deltas: 100% (234/234), done.
root@Wizzy-R7000P:~# ls
 1Wizzy.github.io   GethSpace   asdas  'asdas '   competition   feishu2md
root@Wizzy-R7000P:~# cd 1Wizzy.github.io/
root@Wizzy-R7000P:~/1Wizzy.github.io# ls
Gemfile  LICENSE  README.md  _config.yml  _data  _plugins  _posts  _tabs  assets  feishu2md  index.html  static  tools
root@Wizzy-R7000P:~/1Wizzy.github.io# cd _data/
root@Wizzy-R7000P:~/1Wizzy.github.io/_data# ls
 contact.yml   locales  'locales '   localesᅟᅠ   share.yml
```
