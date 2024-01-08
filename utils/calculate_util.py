# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/3/11 16:33
@description  加减乘除计算
"""

import logging

logging.basicConfig(level=logging.INFO)


def add(a, b):
    result = a + b
    logging.info(f"执行加法操作：{a} + {b} = {result}")
    return result


def subtract(a, b):
    result = a - b
    logging.info(f"执行减法操作：{a} - {b} = {result}")
    return result


def multiply(a, b):
    result = a * b
    logging.info(f"执行乘法操作：{a} * {b} = {result}")
    return result


def divide(a, b):
    if b != 0:
        result = a / b
        logging.info(f"执行除法操作：{a} / {b} = {result}")
        return result
    else:
        raise ValueError("除数不能为零")


if __name__ == '__main__':
    # add(1, 2)
    result = 2097152 / 1024
    print(result)