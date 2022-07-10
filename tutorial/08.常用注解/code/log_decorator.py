# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/5 14:14
@description  日志装饰器
"""

import functools


def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__} with arguments: ({args_str})")
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


@log_decorator
def add(x, y):
    return x + y


if __name__ == '__main__':
    add(3, 5)
