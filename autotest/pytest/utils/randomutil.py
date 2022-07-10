# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/3/25 09:10
@description
"""

import random
from datetime import datetime


class RandomGenerator:

    def __init__(self):
        self.random = random
        self.datetime = datetime

    def random_float(self, start, stop):
        """生成一个指定范围内的随机浮点数"""
        return self.random.uniform(start, stop)

    def random_int(self, start, stop):
        """生成一个指定范围内的随机整数"""
        return self.random.randint(start, stop)

    def random_choice(self, seq):
        """从序列 seq 中随机选择一个元素返回"""
        return self.random.choice(seq)

    def shuffle(self, seq):
        """将序列 seq 随机打乱"""
        self.random.shuffle(seq)

    def formatted_time(self):
        """生成一个格式化的时间"""
        return self.datetime.now().strftime("%Y%m%d%H%M%S")

    def formatted_time2(self):
        """生成一个格式化的时间"""
        return self.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    # 创建一个 RandomGenerator 对象
    rg = RandomGenerator()

    # 生成一个随机浮点数
    f = rg.random_float(1.0, 10.0)

    # 生成一个随机整数
    i = rg.random_int(1, 10)

    # 从序列中随机选择一个元素
    seq = ["red", "green", "blue"]
    color = rg.random_choice(seq)

    # 将序列打乱
    seq = [1, 2, 3, 4, 5]
    rg.shuffle(seq)

    print(rg.formatted_time())
