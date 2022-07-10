#!/usr/bin/env python
# !coding:utf-8

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @pytest.mark.parametrize：把每次循环当做一条用例

@pytest.mark.parametrize(self,argnames, argvalues, indirect=False, ids=None, scope=None))：

argnames	必传，参数名, 以逗号分隔的字符串,表示一个或多个参数名称(key),或参数字符串的列表/元组
argvalues	必传，参数值，若argnames有一个刚单值列表传入，若argnames有多个，以套用元组的列表展示，无组内与参数名一一对应
indirect	为true时，那argnames一定是一个fixture函数名称，argvalues值将传入对应的fixture内，相当于@pytest.fixture(params=)的用法，默认False
ids	标记子用例执行名称，与argvalues数量一致，未指定自动生成,默认None
scope	如果指定，则表示参数的范围。范围用于按参数实例对测试进行分组。它还将覆盖任何fixture函数定义的范围，允许使用测试上下文或配置设置动态范围
"""

import pytest


class TestCase:
    list_demo = [(1, 2, 3), (7, 9, 16), (4, 6, 10), (8, 90, 98)]

    @pytest.mark.parametrize("a, b, result", list_demo)
    def test_result(self, a, b, result):
        print(a + b)
        assert a + b == result

    @pytest.mark.parametrize("a, b, result", list_demo, ids=['case_ids {}'.format(i) for i in list(list_demo)])
    def test_ids(self, a, b, result):
        print(a + b)
        assert a + b == result


if __name__ == '__main__':
    pytest.main()
