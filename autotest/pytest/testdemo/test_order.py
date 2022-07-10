#!/usr/bin/env python
# !coding:utf-8

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @pytest.mark.run(order=n)：控制用例函数执行顺序
安装pytest-ordering：pip install pytest-ordering
在用例函数前面加上@pytest.mark.run(order=n)即可实现按先后顺序执行，其中n为执行顺序。
"""

import pytest


class TestCase:

    @pytest.mark.run(order=2)
    def test_case1(self):
        print("这是 用例1")

    @pytest.mark.mn2
    @pytest.mark.run(order=3)
    def test_case2(self):
        print("这是 用例2")

    @pytest.mark.run(order=1)
    def test_case3(self):
        print("这是 用例3")


if __name__ == '__main__':
    pytest.main()
