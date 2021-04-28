# AioHttp_BestPractices
AioHttp最佳实践

> **说明**：在使用之前先需要了解协程,事件循环(Event Loop),回调(驱动生成器),IO多路复用(epoll)等相关知识,方可快速上手
> 可以先尝试查阅Flask最佳实践:https://github.com/yangyuexiong/Flask_BestPractices

```text
AioHttp_BestPractices
├── ApplicationExample.py(应用实例)
├── Pipfile(环境依赖)
├── Pipfile.lock
├── README.md
├── app
│   ├── __init__.py
│   ├── all_reference.py(通用统一导入)
│   ├── api
│   │   ├── __init__.py(url统一导入)
│   │   ├── index
│   │   │   ├── __init__.py
│   │   │   └── index.py
│   │   └── login
│   │       ├── __init__.py
│   │       └── login.py
│   ├── models(模型)
│   │   └── __init__.py
│   └── static(静态文件)
│       └── __init__.py
├── common(公共类)
│   ├── __init__.py
│   └── libs
│       ├── __init__.py
│       ├── api_result.py
│       └── tools.py
├── config(配置文件)
│   ├── __init__.py
│   ├── config.py
│   ├── dev.ini
│   ├── prod.ini
│   └── uat.int
├── registry(统一注册)
│   ├── __init__.py
│   ├── api_register.py
│   ├── conf_register.py
│   ├── db_register.py
│   └── hook_register.py
└── run.py

```

## 待补充