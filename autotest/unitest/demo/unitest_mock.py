# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 20:44
@description  mock：模拟数据
"""

import unittest
from unittest import mock


class Test(unittest.TestCase):
    def test_01(self):
        str = mock.Mock(return_value={"result": "success"})
        print("mock数据")
        print(str)


if __name__ == '__main__':
    unittest.main()
