#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2022/2/12 11:51
@description pytest测试类
"""

import time
import pytest
from autotest.pytest.utils import assert_util


class TestCase:
    def fun(self, x, y):
        return x + y

    def testcase_01(self):
        assert self.fun(1, 2) == 3

    def testcase_02(self):
        assert self.fun(1, 2) == 3

    print("=====================================================================")

    @pytest.fixture()
    def before(self):
        print("------->before")

    @pytest.mark.flaky(reruns=5, reruns_delay=2)
    def test_retry(self):
        assert 1 == 2
        print("重试机制")

    def test_success(self):
        print("断言成功")
        assert 1

    def test_fail(self):
        print("断言失败")
        assert 0

    print("=====================================================================")

    def add(self, a, b):
        return a + b

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2],
        [2, 2, 4],
        [3, 3, 6],
        [4, 4, 8],
        [5, 5, 10]
    ])
    def test_add_list(self, a, b, expect):
        assert self.add(a, b) == expect

    @pytest.mark.parametrize('a,b,expect', [
        (1, 1, 2),
        (2, 2, 4),
        (3, 3, 6),
        (4, 4, 8),
        (5, 5, 10)
    ])
    def test_add_tuple(self, a, b, expect):
        assert self.add(a, b) == expect

    @pytest.mark.parametrize('data', [
        {'a': 1, 'b': 1, 'expect': 2},
        {'a': 5, 'b': 5, 'expect': 10}
    ])
    def test_add_dict(self, data):
        assert self.add(data['a'], data['b']) == data['expect']

    print("=====================================================================")

    def test_assert(self):
        assert_util.assert_equal(1, 2)

    def add(self, a, b):
        try:
            return a + b
        except Exception as e:
            return e.args[0]

    print("=====================================================================")

    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 2),
        (1.0, 1.0, 2.0),
        (1, 1.0, 2.0),
        (1, 0, 1),
        ('', '', ''),
        ('a ', 'b', 'a b'),
        (0, '', "unsupported operand type(s) for +: 'int' and 'str'"),
        (1, 'a', "unsupported operand type(s) for +: 'int' and 'str'"),
        (1.0, 'a', "unsupported operand type(s) for +: 'float' and 'str'"),
    ])
    def test_add(self, a, b, result):
        time.sleep(1)
        assert self.add(a, b) == result


if __name__ == '__main__':
    pytest.main()
