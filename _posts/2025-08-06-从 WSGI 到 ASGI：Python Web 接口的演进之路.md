---
title: "从 WSGI 到 ASGI：Python Web 接口的演进之路"
date: 2025-08-06 21:58
categories: ['Blog']
tags: ['Python', 'WSGI', 'ASGI']
---

WSGI 和 ASGI 是 Python Web 框架中两种常见的服务网关接口规范，用于定义 Web 应用程序与服务器之间如何通信。它们的区别主要体现在是否支持异步通信。

## 🧩 一、WSGI（Web Server Gateway Interface）

WSGI（Web Server Gateway Interface）是 Python 官方在 PEP 333 中提出的 Web 应用与服务器之间的标准通信协议，它的目标是让 Web 框架和 Web 服务器可以解耦、互换。

- 用途：是 Python Web 应用的 同步接口标准。

- 设计初衷：用于处理标准的 HTTP 请求，适用于大多数传统 Web 应用。

- 核心特点：

    - 只支持 同步（阻塞） 调用。

    - 每个请求由一个线程或进程处理。

    - 无法高效处理 WebSocket、长轮询等异步任务。

- 典型框架：Flask、Django（早期版本）、Bottle、Pyramid。

- 示意图：
```
Browser ↔ Web Server ↔ WSGI Server ↔ Python Web App
```

## 🧩 二、ASGI（Asynchronous Server Gateway Interface）

随着 Web 应用对实时通信、高并发的需求增长，WSGI 显得力不从心。于是，ASGI（Asynchronous Server Gateway Interface）应运而生，它是 WSGI 的 “异步时代继任者”。

- 用途：是对 WSGI 的升级，支持 异步编程。

- 设计初衷：为了适应现代 Web 应用对 WebSocket、HTTP/2、长轮询等异步需求。

- 核心特点：

    - 支持 异步（非阻塞）和同步 调用。

    - 更适合实时性强的应用，如聊天、推送、数据流处理。

    - 能处理 HTTP 和 WebSocket。

- 典型框架：FastAPI、Django（3.0+ 支持）、Starlette、Quart。

- 示意图：
```
Browser ↔ Web Server ↔ ASGI Server ↔ Async Python Web App
```

## 🔍三、 WSGI vs ASGI 对比一览


| 特性        | WSGI                    | ASGI                     |
| --------- | ----------------------- | ------------------------ |
| 异步支持      | ❌ 仅支持同步                 | ✅ 同时支持同步 + 异步            |
| WebSocket | ❌ 不支持                   | ✅ 原生支持                   |
| 性能并发      | 中（阻塞，线程/进程）             | 高（非阻塞，事件驱动）              |
| 应用场景      | 表单、管理后台、CMS             | 实时推送、聊天、IoT、WebSocket    |
| 典型框架      | Flask、Django         | FastAPI、Django（v3.0 以后） |
| 服务端建议     | Gunicorn + WSGI workers | Uvicorn、Daphne、Hypercorn |



## ✅ 四、总结
- WSGI：适用于传统同步 Web 应用，结构稳定，生态成熟。

- ASGI：适用于现代异步 Web 应用，可支持更高的并发和实时通信。