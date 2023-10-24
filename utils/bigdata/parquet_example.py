# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/11/14 10:46
@description  读取 parquet 文件

pip install pyarrow
"""

import pyarrow.parquet as pq


def demo1():
    # 读取Parquet文件
    path = '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/test_sft-00000-of-00001-fe658ed8e3578d4a.parquet'
    table = pq.read_table(path)

    # 将Parquet文件转换为Pandas DataFrame对象
    df = table.to_pandas()

    # 打印DataFrame
    print(df)


def demo2():
    # 逐块读取Parquet文件
    path = '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/test_sft-00000-of-00001-fe658ed8e3578d4a.parquet'
    # 读取Parquet文件
    table = pq.read_table(path)

    # 将Parquet文件转换为Pandas DataFrame对象
    df = table.to_pandas()

    # 逐块处理数据
    chunksize = 100000
    chunks = [df[i:i + chunksize] for i in range(0, df.shape[0], chunksize)]
    for chunk in chunks:
        # 处理数据块
        print(chunk)


if __name__ == '__main__':
    # demo1()
    demo2()
