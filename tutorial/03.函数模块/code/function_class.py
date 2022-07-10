# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/7 13:56
@description  函数和方法的异同

在 Python 中，函数和方法都是用来执行特定任务的代码块，但它们有以下几个区别:
语法不同：函数是使用 def 语句定义的，而方法是使用 class 语句或继承定义的。
作用域不同：函数的作用域只局限于定义它的模块或类中，而方法的作用域取决于实例化和调用它的对象。
返回值不同：函数默认返回值为函数的参数值，而方法的返回值为所调用的实例的返回值。
引用方式不同：函数是内置类型之一，可以使用方括号 ([]) 来调用，而方法需要使用对象指针 (.) 来调用。
对象属性不同：函数不是对象，而方法是基于对象的。这意味着可以通过对象指针访问方法，而不需要实例化对象。
"""


def function():
    print("This is a function")


class MyClass:
    def method(self):
        print("This is a method")


if __name__ == '__main__':
    my_obj = MyClass()
    function_obj = function()
    my_obj.method()
