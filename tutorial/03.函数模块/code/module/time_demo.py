#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author        weimenghua
@time          2021/7/25 10:04
@description   time 模块：时间 datetime 模块：时间
"""

import time
import datetime


def time_demo():
    print("当前时间戳：", time.time())
    print("本地时间：", time.localtime(time.time()))
    print("本地时间：", time.asctime(time.localtime(time.time())))
    print("本地时间：", time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    print("本地时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def datetime_demo():
    print('当前日期：', datetime.datetime.now().strftime('%Y-%m-%d'))
    print('当前年份：', datetime.datetime.now().strftime('%Y'))
    print('当前月份：', datetime.datetime.now().strftime('%m'))


if __name__ == '__main__':
    # time_demo()
    datetime_demo()
