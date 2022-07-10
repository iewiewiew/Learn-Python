# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/7/2 08:55
@description  Python 接入 Sentry
"""

import sentry_sdk


def demo():
    sentry_sdk.init("http://ea9261e951fa4dca81a31d1ef15fab21@127.0.0.1:9000/2")
    division_by_zero = 1 / 0
    print(division_by_zero)


if __name__ == '__main__':
    demo()
