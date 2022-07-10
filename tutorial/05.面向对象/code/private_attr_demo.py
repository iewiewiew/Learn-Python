# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/24 14:00
@description  私有化属性
"""


class MyClass:
    def __init__(self):
        self._private_attr = 123

    def public_method(self):
        print("This is a public method.")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._private_attr


if __name__ == '__main__':
    my_obj = MyClass()
    print(my_obj._private_attr)  # 输出:123
    my_obj.public_method()       # 输出:This is a public method.
