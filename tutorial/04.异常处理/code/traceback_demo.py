#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author        weimenghua
@time          2020/7/12 16:27
@description   异常处理
"""

import traceback


def zero1():
    try:
        a = 1 / 0
        print(a)
    except:
        print('1/0, 发生异常了')


def zero2():
    try:
        a = 1 / 0
        print(a)
    except Exception:
        print('traceback：1/0, 发生异常了')
        traceback.print_exc()


def zero3():
    try:
        raise Exception('raise 主动抛出异常，异常后的代码不再执行')
        a = 1 / 0
        print(a)
    except Exception as e:
        print(e)


def zero4():
    try:
        raise Exception('raise 主动抛出异常，异常后的代码不再执行')
        a = 1 / 0
        print(a)
    except Exception as e:
        print(e)
    finally:
        print('一定要打印出来！')


def zero5():
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(e)


def zero6():
    try:
        1/0
    except Exception:
        error_message = traceback.format_exc()   # 使用 traceback.format_exc() 函数获取详细的堆栈跟踪信息
        print(error_message)


def zero7():
    try:
        result = 100/1
    except ZeroDivisionError:
        print('除数不能为0')
    else:
        print('计算结果: ', result)


class MyCustomException(Exception):
    print('自定义异常')


def zero8():
    try:
        1/0
    except MyCustomException as e:
        print(e)


if __name__ == '__main__':
    # zero1()
    # zero2()
    # zero3()
    # zero4()
    # zero5()
    # zero6()
    # zero7()
    zero8()
