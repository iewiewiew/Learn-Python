# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/27 17:32
@description  自动导入代码中使用到的Python库

pip install pyforest -i https://pypi.tuna.tsinghua.edu.cn/simple
"""

import pyforest

list_ = [n for n in dir(pyforest)]

print(f'python内置库的总数是：{str(len(list_))}')
# python内置库的总数是：105

print(list_)
