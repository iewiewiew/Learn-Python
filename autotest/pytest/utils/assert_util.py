# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/16 17:15
@description  封装断言
"""


def assert_equal(actual, expected):
    assert actual == expected, "实际结果为:{0}, 预期结果为:{1}".format(actual, expected)


def assert_not_equal(a, b):
    assert a != b, "{0}等于{1}".format(a, b)


def assert_in(a, b):
    assert a in b, "{0}不包含{1}".format(b, a)


def assert_true(value):
    assert value, "{0} 为假".format(value)


if __name__ == '__main__':
    assert_equal(1, 1)
