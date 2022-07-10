# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 14:18
@description  None的用法
None常用作函数的默认返回值，表示没有明确的返回结果。
None可以用作占位符，在某些逻辑中表示待填充的位置。
None还可以用于初始化变量，将其置为初始空状态。
"""


# 定义一个函数，返回两个数的和
def add_numbers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None

# 调用函数并输出结果
result = add_numbers(10, 20)
if result is not None:
    print("Sum:", result)
else:
    print("Invalid input")