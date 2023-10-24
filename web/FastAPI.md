[TOC]

<h1 align="center">FaseAPI</h1>

> By：weimenghua
> Date：2023.10.26
> Description：

**参考资料**  
[FastAPI 官网](https://fastapi.tiangolo.com/)
[FastAPI 源码](https://github.com/tiangolo/fastapi)



## 一、FastAPI 简介

FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.8+ 并基于标准的 Python 类型提示。

关键特性:  
- 快速：可与 NodeJS 和 Go 并肩的极高性能（归功于 Starlette 和 Pydantic）。最快的 Python web 框架之一。
- 高效编码：提高功能开发速度约 200％ 至 300％。*
- 更少 bug：减少约 40％ 的人为（开发者）导致错误。*
- 智能：极佳的编辑器支持。处处皆可自动补全，减少调试时间。
- 简单：设计的易于使用和学习，阅读文档的时间更短。
- 简短：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少。
- 健壮：生产可用级别的代码。还有自动生成的交互式文档。
- 标准化：基于（并完全兼容）API 的相关开放标准：OpenAPI (以前被称为 Swagger) 和 JSON Schema。



## 二、FastAPI 教程

[fastapi](https://fastapi.tiangolo.com/reference/fastapi/)

```
安装 fastapi
pip install fastapi

安装 uvicorn
pip install "uvicorn[standard]"
```

```
启动服务
uvicorn <class_name>:app
uvicorn fastapi01:app

生成文档，文档地址：http://127.0.0.1:8000/docs，http://127.0.0.1:8000/openapi.json
uvicorn <class_name>:app --reload
```

```  
HTTP 请求方法：
@app.get('/')
@app.put('/')
@app.patch('/')
@app.delete('/')
```


FastAPI 使用 Pydantic 模型进行数据验证，确保输入数据的类型正确，并提供有关数据验证错误的详细信息。