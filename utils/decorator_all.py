# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/10 18:18
@description  装饰器集合
"""


def method_decorator(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        print("方法名:", method_name)
        return func(*args, **kwargs)

    return wrapper