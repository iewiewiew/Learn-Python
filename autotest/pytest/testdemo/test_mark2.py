# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/28 14:47
@description
"""
import pytest


# todo：没成功
@pytest.mark.dependency()
def test_setup():
    # 设置测试环境
    print("11111111111")
    assert True


@pytest.mark.dependency(depends=['test_setup'])
def test_execution():
    # 测试用例依赖于test_setup函数
    print("2222222222")
    assert True


@pytest.mark.dependency(depends=['test_execution'], scope='session')
def test_cleanup():
    # 在所有测试用例运行结束之后执行清理操作
    print("3333333333")
    assert True
