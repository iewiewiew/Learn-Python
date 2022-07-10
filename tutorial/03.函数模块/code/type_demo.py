# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 14:14
@description  type函数是Python的内置函数，用于获取对象的类型

区别与应用：
虽然isinstance和type都可以用于判断对象的类型，但它们存在一些区别和应用场景：
isinstance函数可以用于判断对象是否属于某个类或其子类，而type函数只能获取对象的类型，无法判断是否为子类。
isinstance函数可以接受一个类型对象的元组作为第二个参数，用于判断对象是否属于多个类型之一。这在需要同时判断多个类型时非常有用。
type函数返回的是对象的具体类型，而isinstance函数返回的是布尔值。
综上所述，isinstance和type在类型判断中都有各自的用途和特点。在实际编程中，我们需要根据具体的需求选择合适的方法来判断对象的类型。
"""


class Person:
    pass


student = Person()
print(type(student))  # 输出：<class '__main__.Person'>
