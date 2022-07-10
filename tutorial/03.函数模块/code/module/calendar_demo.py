#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2021/7/25 15:48
@description calendar模块：日历
"""

import calendar
import datetime


def demo():


    cal = calendar.month(2023, 5)
    print('指定月历：', cal)


if __name__ == '__main__':
    demo()
