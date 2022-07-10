#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2022/2/16 22:33
@description 装饰器

装饰器定义：装饰器便于代码复用, 将函数作为参数传给装饰器函数, 拓展原来函数功能的一种函数。
装饰器作用：装饰器就是在不修改被装饰器对象源代码以及调用方式的前提下为被装饰对象添加新功能(增强函数功能但是又不修改原函数, 抽离函数中与函数本身无关的功能进行复用)。
应用场景：插入日志、性能测试、事务处理、 Web 权限校验、Cache 等。
"""

import time


def funA(func):
    """
    1、无参函数装饰器
    把@funA 放到 funA_test()函数的定义处，相当于执行了语句：funA_test = funA(funA_test)
    """
    print('1、装饰器函数 funA 增强 %s()' % func.__name__)
    func()


@funA
def funA_test():
    print('1、原函数 funA_test')


def funB(func):
    """
    2、不定长参数函数装饰器
    wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在 wrapper()函数内，首先打印日志，再紧接着调用原始函数。
    """
    def wrapper(*args, **kwargs):
        print('2、装饰器函数 funB 增强 %s()' % func.__name__)
        func(*args, **kwargs)
    return wrapper


@funB
def funB_test(x, y):
    print('2、原函数 funB_test', x, '+', y, '=', x + y)


def funC(parameter):
    """
    3、参数装饰器
    """
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if parameter == 'task1':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("3、装饰器函数 funC the task1 run time is :", stop - start)
            elif parameter == 'task2':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("3、装饰器函数 funC the task2 run time is :", stop - start)

        return wrapper

    return outer_wrapper


@funC(parameter='task1')
def funC_test1():
    time.sleep(2)
    print("3、原函数 funC_test1")


@funC(parameter='task2')
def funC_test2():
    time.sleep(2)
    print("3、原函数 funC_test2")


def funD1(func):
    """
    4、嵌套装饰器
    @funD1
    @funD2
    @funD3
    def funCTest():
        pass
    等价于：funD_test = funD1(funD2(funD3(funD_test)))
    """
    print('4、装饰器函数 funD1')
    func


def funD2(func):
    print('4、装饰器函数 funD2')
    func


def funD3(func):
    print('4、装饰器函数 funD3')
    func


@funD1
@funD2
@funD3
def funD_test():
    print('4、原函数 funD_test')


def timeit(func):
    """
    5、时间间隔参数装饰器
    """
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('5、装饰器函数 timeit', end - start)

    return wrapper


@timeit
def timeit_test():
    time.sleep(3)
    print('5、原函数 timeit_test')


def f1():
    """
    闭包
    定义：闭包就是能够读取外部函数内的变量的函数。
    作用1：闭包是将外层函数内的局部变量和外层函数的外部连接起来的一座桥梁。
    作用2：将外层函数的变量持久地保存在内存中。
    函数 f2被包括在函数 f1内部，这时 f1内部的所有局部变量，对 f2都是可见的。但是反过来就不行，f2内部的局部变量，对 f1就是不可见的。
    有一个外层函数的局部变量 n，有一个内层函数 f2，f2 里面可以访问到 n 变量，那这 f2就是一个闭包。
    """
    n = 999
    def f2():
        print(n)
    return f2


if __name__ == '__main__':
    funB_test(2, 4)
    funC_test1()
    funC_test2()
    funD_test
    timeit_test()
