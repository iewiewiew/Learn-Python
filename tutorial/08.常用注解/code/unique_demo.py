# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/4 13:59
@description  @unique 找出重复值
"""

from enum import Enum, unique


@unique
class Weekday(Enum):
    monday = 1
    tusday = 2
    wensdday = 3
    thursday = 4
    friday = 5


def demo():
    for n, y in Weekday.__members__.items():
        print(n, '--', y, '--', y.value)

    f = Weekday.thursday
    print(f.value)


if __name__ == '__main__':
    demo()
