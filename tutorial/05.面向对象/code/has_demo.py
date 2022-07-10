# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/5 10:39
@description  hasattr() 函数 + getattr() 函数 + setattr() 函数

hasattr()函数用于判断一个对象是否具有指定的属性。其基本语法为：hasattr(object, name)
- object：表示要检查的对象。
- name：表示要检查的属性名，可以是字符串或标识符。

getattr()函数用于获取一个对象的属性的值。其基本语法为：getattr(object, name[, default])
- object：表示要获取属性值的对象。
- name：表示要获取的属性名，可以是字符串或标识符。
- default：可选参数，表示当属性不存在时的默认值。如果不提供default参数，并且属性不存在，将会抛出AttributeError异常。

setattr()函数用于设置一个对象的属性值。其基本语法为：setattr(object, name, value)
- object：表示要设置属性值的对象。
- name：表示要设置的属性名，可以是字符串或标识符。
- value：表示要设置的属性值。
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('wei', 18)
    print(hasattr(person, 'name'))  # True
    print(hasattr(person, 'tmp'))  # False

    print(getattr(person, 'name'))
    print(getattr(person, 'age'))
    # print(getattr(person, 'tmp'))

    setattr(person, "name", "wei2")
    setattr(person, "age", "19")
    print(person.name)
    print(person.age)
