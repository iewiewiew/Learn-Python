#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2021/10/10 9:59
@description @retry() 重试
"""

from tenacity import *


@retry()
def demo():
    print('执行 demo 一直重试')
    raise Exception('手动抛出异常')


@retry(stop=stop_after_attempt(3))
def demo1():
    print('执行 demo 重试 3 次后停止')
    raise Exception('手动抛出异常')


@retry(stop=stop_after_delay(5))
def demo2():
    print('执行 demo 重试 5 秒后停止')
    raise Exception('手动抛出异常')


@retry(stop=(stop_after_delay(2) | stop_after_attempt(10)))
def demo3():
    print('执行 demo 重试 2 秒或者重试 10 次停止')
    raise Exception('手动抛出异常')


@retry(wait=wait_fixed(5))
def demo4():
    print('执行 demo 每次重试的等待时间 5 秒')
    raise Exception('手动抛出异常')


@retry(wait=wait_random(min=1, max=5))
def demo5():
    print('执行 demo 重试间隔时间 1-5 秒随机')
    raise Exception('手动抛出异常')


@retry(wait=wait_fixed(3) + wait_random(0, 2))
def demo6():
    print('执行 demo 随机等待 0-2 秒和每次等待 3 秒重试都满足才会重试')
    raise Exception('手动抛出异常')


@retry(retry=retry_if_exception_type(TypeError))
def demo7():
    print('执行 demo 指定 TypeError 才会重复')
    print('a' + 1)


@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(3))
def demo8():
    print('执行 demo')
    raise Exception('手动抛出异常')


@retry(exceptions=(Exception), tries=5, delay=3)
def demo9():
    print('执行 demo 在遇到 Exception 异常（也可以是其它异常）时重试5次，每次重试间隔3秒 Exception 是最大错误级别')
    tmp = 1 / 0
    print('遇到异常重试')


if __name__ == '__main__':
    demo()
    # demo1()
    # demo2()
