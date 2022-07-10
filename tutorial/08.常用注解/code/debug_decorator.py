# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 14:46
@description  Debug 装饰器
"""


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Debugging {func.__name__} - args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@debug
def complex_data_processing(data, threshold=0.5):
    return None


if __name__ == '__main__':
    complex_data_processing(123, threshold=0.5)
