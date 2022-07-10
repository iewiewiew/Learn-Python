# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/6/19 14:45
@description

@dataclass 是 Python 3.7 引入的一个装饰器，用于简化创建类的过程。它使得定义一个数据类变得更加简单和易读，而且还提供了一些默认实现，例如 __init__ 和 __repr__ 方法。
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Person:
    name: str
    age: int
    addresses: List[str] = field(default_factory=list)
