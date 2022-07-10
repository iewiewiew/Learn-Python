#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @pytest.fixture()：测试脚手架

说明：fixture用来完成那些需要多次重复执行的用例，比如需要先退出，再更换其他用户登录。
我们可以把用于退出和登录的用例的函数比如叫做A函数，在A函数的前面加上@pytest.fixture()装饰器，
这样，这个A函数就可以被其他函数直接调用了，只要其他用例函数在执行前需要有先进行退出再更换其他用户登录的操作，都可以直接调A函数。

查看内置 pytest fixture 的类型：pytest --fixtures

Fixture 作用域
fixture 在第一次被测试请求时被创建，并根据它们的作用域被销毁:
function: 默认作用域，fixture在测试结束时销毁。
class: 在class中的最后一个测试拆除期间，fixture被销毁。
module: 在module的最后一次测试拆卸时，fixture被破坏。
package: 在package中的最后一次测试拆卸时，fixture被破坏。
session: fixture在测试session结束时被销毁。
Pytest一次只缓存一个fixture的一个实例，这意味着当使用参数化的fixture时，Pytest可以在给定范围内多次调用一个fixture。
优先级：session > package > module > class > function，优先级高的会在低的fixture之前先实例化。
"""

import pytest


@pytest.fixture()
def fix():
    print("========执行fix========")


@pytest.fixture()
def fix1():
    print("========执行fix1========")


@pytest.fixture()
def fix2():
    print("========执行fix2========")


@pytest.fixture()
def fix_scope(scope="session"):
    print("========执行fix_scope========")


# autouse fixture (自动适配fixture)是使所有测试自动请求它们的一种方便的方法
@pytest.fixture(autouse=True)
def fix_autouse():
    print("========执行fix_autouse========")


# 参数化 fixture
@pytest.fixture(autouse=True, params=["参数1", "参数2"], ids=["case1", "case2"])
def fix_params(request):
    print("========执行fix_params========")
    print(request.param)


def test_case1(fix):
    print("执行用例1")


def test_case2(fix1, fix2):
    print("执行用例2")


class Test_case:

    def test_case1(self, fix1):
        print("执行用例11")

    def test_case2(self, fix2):
        print("执行用例22")

    def test_case3(self, fix3):
        print("执行用例33")

    def test_case4(self, fix, fix1, fix2, fix3):
        print("执行用例44")


if __name__ == '__main__':
    pytest.main()
