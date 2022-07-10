# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/6/19 14:05
@description  BaseModel

Pydantic是一个Python库，用于数据验证和解析。其主要功能是定义数据模型和验证输入数据是否符合这些模型。
Pydantic的主要作用包括：
数据验证：Pydantic可以通过定义数据模型来验证输入数据是否符合预期的格式、类型和范围。这可以帮助开发人员在程序运行之前捕获错误，从而提高代码的可靠性和可维护性。
数据解析：Pydantic可以将输入数据解析成Python对象，方便后续的操作和处理。它支持从各种数据源中解析数据，包括JSON、XML、YAML等格式。
序列化：Pydantic可以将Python对象序列化为各种格式的数据，包括JSON、XML、YAML等格式。这对于数据的传输和存储非常有用。
自动生成API文档：Pydantic可以通过定义数据模型自动生成API文档，包括数据模型的字段、类型、默认值等信息。这对于API的开发和文档编写非常有帮助。
"""

from pydantic import BaseModel, validator


class User(BaseModel):
    id: int
    name: str
    email: str = None


class Blog(BaseModel):
    name: str

    @validator('name')
    def check_name_length(cls, name):
        if(len(name) < 3):
            raise ValueError('name too short')
        return name


if __name__ == '__main__':
    user = User(id=1, name='wei', email='123456@qq.com')
    print(user.dict())
    print(user.json())

    blog = Blog(name='ok')
    print(blog.json())

