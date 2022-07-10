#!/usr/bin/env python
# !coding:utf-8

"""
@author      weimenghua
@time        2022/2/12 11:51
@description 前置后置

pytest的前置和后置包括如下几种：
模块级（setup_module/teardown_module）开始于模块始末，作用于全局（总用各执行一次）
函数级（setup_function/teardown_function）仅对函数用例生效。（即不在类中，每个函数执行一次）
类级（setup_class/teardown_class）只在类中前后运行一次。（在类中）
方法级（setup_method/teardown_method）开始于方法始末（在类中，每个方法执行一次）
类里面的（setup/teardown）运行在调用方法的前后（每个方法执行一次）

setup_class是在所有用例执行前运行的，teardown_class是在所有用例执行完成后运行的。
setup_method是在每一条用例执行前，且在setup执行前运行的，teardown_method是在每一条用例执行完成后，且在teardown执行完成后运行的。
setup是在每条用例执行前运行，teardown是在每条用例执行完成后运行。
所以，他们的顺序是：
setup_class-
setup_method-setup-用例1-teardown-teardown_method-
setup_method-setup-用例2-teardown-teardown_method-
setup_method-setup-用例n-teardown-teardown_method-
……
teardown_class
"""

import pytest


class TestCase:

    def setup_module(self):
        print('这是setup_module')

    def teardown_module(self):
        print("这是teardown_module")

    def setup_function(self):
        print("这是setup_function")

    def teardown_function(self):
        print("这是 teardown_function")

    def setup_class(self):
        print("这是setup_class")

    def teardown_class(self):
        print("这是teardown_class")

    def setup_method(self):
        print("这是setup_method")

    def teardown_method(self):
        print("这是teardown_method")

    def setup(self):
        print("这是setup")

    def teardown(self):
        print("这是teardown")

    def test_one(self):
        print("这是用例1")

    def test_two(self):
        print("这是用例2")


if __name__ == '__main__':
    pytest.main()
