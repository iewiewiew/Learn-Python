# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 10:15
@description  matplotlib模块：画图
"""

import matplotlib.pyplot as plt


def demo():
    # 保存x轴数据的列表
    x_values = [x for x in range(1, 11)]
    # 保存y轴数据的列表
    y_values = [x ** 2 for x in range(1, 11)]
    # 设置图表的标题以及x和y轴的说明
    plt.title('Square Numbers')
    plt.xlabel('Value', fontsize=18)
    plt.ylabel('Square', fontsize=18)
    # 设置刻度标记的文字大小
    plt.tick_params(axis='both', labelsize=16)
    # 绘制折线图
    plt.plot(x_values, y_values)
    plt.show()


if __name__ == '__main__':
    demo()
