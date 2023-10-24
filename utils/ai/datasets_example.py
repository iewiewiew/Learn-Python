# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/11/16 15:24
@description  加载数据集

数据集缓存目录：cd ~/.cache/huggingface/datasets
"""

import datasets


def demo():
    # 加载单个数据集
    raw_datasets = datasets.load_dataset('squad')
    # 加载多个数据集
    raw_datasets = datasets.load_dataset('glue', 'mrpc')


if __name__ == '__main__':
    demo()
