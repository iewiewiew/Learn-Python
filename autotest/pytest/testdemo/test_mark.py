#!/usr/bin/env python
# !coding:utf-8

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @pytest.mark.mn1：标记装饰器

列出所有标记：pytest --markers
内置标记：
usefixtures ——在测试函数或类上使用fixture
filterwarnings —过滤测试函数的某些警告
skip —总是跳过一个测试函数
skipif -如果满足某个条件，则跳过某个测试函数
Xfail ——如果满足某个条件，则产生一个“预期失败”的结果
parametrize ——对同一个测试函数执行多个调用
"""

import pytest


# 在类中使用fixtures
@pytest.mark.usefixtures("demo_fixture")
class TestCase():

    def setup_module(self):
        print('这是setup_module')

    def teardown_module(self):
        print("这是teardown_module")

    def setup_function(self):
        print("这是setup_function")

    def teardown_function(self):
        print("这是teardown_function")

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

    @pytest.mark.mn1
    def test_case1(self):
        print("这是 用例1")

    @pytest.mark.mn2
    def test_case2(self):
        print("这是 用例2")

    @pytest.mark.xfail(2 > 1, reason="标记为预期失败")
    def test_case3(self):
        print("这是 用例3")
        assert 0

    @pytest.mark.usefixtures("demo_fixture")
    def test_case4(self):
        print("这是 用例4")

    @pytest.mark.skipif("1 > 0", reason="满足条件则跳过")
    def test_case5(self):
        print("这是 用例5")

    # 定义第一个测试函数
    @pytest.mark.dependency()
    def test_setup(self):
        print('测试函数依赖')
        assert True

    # 定义第二个测试函数，并将其标记为“depends_on”第一个测试函数
    @pytest.mark.depends_on(depends=['TestCase::test_setup'])
    def test_execution(self):
        print('在这里执行需要在“test_setup”运行后才能运行的测试代码')
        assert True


if __name__ == '__main__':
    pytest.main()
