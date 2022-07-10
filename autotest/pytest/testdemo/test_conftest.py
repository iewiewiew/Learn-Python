# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/9/2 12:48
@description  测试conftest
"""

import pytest


def test_demo(demo_fixture):
    print("测试conftest")


if __name__ == '__main__':
    pytest.main()