# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/5 16:31
@description  重试装饰器
"""

import functools
import time


def retry_decorator(max_retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            raise Exception(f"Failed after {max_retries} retries")
        return wrapper
    return decorator


@retry_decorator()
def unstable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random error")
    return "Success"


if __name__ == '__main__':
    print(unstable_function())
