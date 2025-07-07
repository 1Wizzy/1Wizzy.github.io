# README
[![Gem Version](https://img.shields.io/gem/v/jekyll-theme-chirpy)][gem]&nbsp;
[![GitHub license](https://img.shields.io/github/license/cotes2020/chirpy-starter.svg?color=blue)][mit]

本项目基于Chirpy Starter主题，通过feishu2md从飞书上下载markdown文档，上传至Github仓库。

整个项目基本实现了全流程CI/CD，可通过GithubAction自动下载文档，自动部署博客。

## 需注意的问题

1. feishu2md 无法正常下载飞书云文档：

   此问题只发生在少量的文档上。

   解决方法：
   - 如果飞书开放平台中feishu2md的权限使用tenant_access_token：
     - 需要通过云文档页面右上方「...」→「...更多」→「添加文档应用」为应用添加权限
     - 确保文档未启用密码保护等额外安全设置
  
   - 如果使用user_access_token：
     - 需要通过文档「分享」功能为当前用户添加权限

其他的问题请看 [Wsine/feishu2md 各种报错问题汇总排查 #71](https://github.com/Wsine/feishu2md/issues/71)

 2. 由于笔记久远，很多链接用的`http`协议，于是在`pages-deploy.yml`中`Test site`移除了检测`http`链接的检测。

    本人并不推荐这种方法，并强烈建议恢复检测。


## 下一步工作

1. Chirpy 模板只渲染正文markdown中的h2~h6，故需修改从飞书上下载的markdown文件 ✅

2. 修改从飞书下载的markdown文件的其他问题 ❎

## 本项目所用到的开源项目

- [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/wiki)

- [feishu2md](https://github.com/Wsine/feishu2md)

## 许可证

本项目以 [MIT][mit] License 发布.

[gem]: https://rubygems.org/gems/jekyll-theme-chirpy
[chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy/
[CD]: https://en.wikipedia.org/wiki/Continuous_deployment
[mit]: https://github.com/cotes2020/chirpy-starter/blob/master/LICENSE
