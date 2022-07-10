# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/6/19 15:07
@description

isinstance() 是 Python 内置函数之一，用于检查一个对象是否属于指定的类或类型。其函数签名为：isinstance(object, classinfo)
其中，object 表示要检查的对象，classinfo 表示要检查的类或类型。如果 object 属于 classinfo 类或类型的对象，则返回 True，否则返回 False。
classinfo 参数可以是一个类、类型、元组或抽象基类。
"""


class MyClass:
    pass


if __name__ == '__main__':
    # 检查一个对象是否属于指定的类
    obj = MyClass()
    print(isinstance(obj, MyClass))  # True
    print(isinstance(obj, int))  # False

    # 检查一个对象是否属于指定的类型
    print(isinstance('hello', str))  # True
    print(isinstance(123, int))  # True
    print(isinstance(3.14, float))  # True

    # 检查一个对象是否属于多个类或类型中的任意一个
    print(isinstance('hello', (int, float, str)))  # True
    print(isinstance(123, (float, str)))  # False
