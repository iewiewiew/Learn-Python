# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/3/31 08:37
@description

python中eval的用法：
python eval() 函数的功能：将字符串str当成有效的表达式来求值并返回计算结果。
语法：eval(source[, globals[, locals]]) -> value
参数：
source：一个Python表达式或函数compile()返回的代码对象
globals：可选。必须是dictionary
locals：可选。任意map对象
如果提供了globals参数，那么它必须是dictionary类型；如果提供了locals参数，那么它可以是任意的map对象。
python的全局名字空间存储在一个叫globals()的dict对象中；局部名字空间存储在一个叫locals()的dict对象中。我们可以用print (locals())来查看该函数体内的所有变量名和变量值。
"""

