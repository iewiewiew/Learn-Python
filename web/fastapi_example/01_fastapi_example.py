# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/25 10:11
@description  FastAPI 例子
"""

import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel, Field
from __future__ import annotations


# 定义模型的元数据
class Item(BaseModel):
    name: str
    description: str = Field(..., description="描述信息")


# http://127.0.0.1:8000/docs
# app = FastAPI()

# http://127.0.0.1:8000/redoc
# 定义应用app对象的元数据
app = FastAPI(title="My API", description="API 描述", summary="API 总结？", version="v1.0.0", redoc_url="/redoc")


@app.get('/')
def home():
    """
    curl -X GET http://127.0.0.1:8000/
    """
    return 'hello world'


# 定义路由的元数据
@app.get('/users/{user_id}', summary="路由标题", description="路由描述说明")
def get_test(user_id: int):
    """
    curl -X GET http://127.0.0.1:8000/users/123
    """
    return {'user_id': user_id}


@app.post('/users')
def post_test():
    """
    curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "age": 25}' http://127.0.0.1:8000/users
    """
    return 'Is a post request'


@app.post('/submit')
def post_form_test(city: str = Form(...)):
    """
    curl --location '127.0.0.1:8000/submit' --form 'city="shanghai"'
    """
    return {'city': city}


@app.post('/upload')
def upload_file_test(file: UploadFile = File(...)):
    """
    curl --location '127.0.0.1:8000/upload' --header 'Content-Type: multipart/form-data' --form 'file=@"/Users/menghuawei/PycharmProjects/Learn-Python/web/fastapi01.py"'
    """
    return {'name': file.filename}


if __name__ == '__main__':
    uvicorn.run(app)

    """
    启动服务：uvicorn 01_fastapi_example:app
    生成文档：uvicorn 01_fastapi_example:app --reload，文档地址：http://127.0.0.1:8000/docs，http://127.0.0.1:8000/openapi.json
    """
