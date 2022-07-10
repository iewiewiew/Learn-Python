#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @pytest.mark.flaky：失败重试
安装pytest-rerunfailures：pip install pytest-rerunfailures
"""

import pytest


class TestCase():
    def fun(self, x, y):
        return x + y

    rerun_times = 3
    jiange = 3

    @pytest.mark.flaky(reruns=rerun_times, reruns_delay=jiange)
    def test_case1(self):
        print("重试")
        assert self.fun(1, 2) == 4

    def test_case2(self):
        assert self.fun(1, 2) == 3


if __name__ == '__main__':
    pytest.main()
