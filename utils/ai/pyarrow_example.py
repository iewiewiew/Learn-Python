# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/11/16 15:42
@description  解析 .arrow 文件，注：未实践成功

pyarrow是一个用于处理大型数据集的库，它支持多种数据格式，包括Parquet、Feather和Arrow等。
"""

import pyarrow as pa


def demo():
    path = '/Users/menghuawei/.cache/huggingface/datasets/glue/mrpc/1.0.0/dacbe3125aa31d7f70367a07a8a9e72a5a0bfeb5fc42e75c9db75b96da6053ad/glue-train.arrow'

    # 读取.arrow文件
    table = pa.ipc.open_file(path).read_all()

    # 将.arrow文件转换为Pandas DataFrame对象
    df = table.to_pandas()

    # 打印DataFrame
    print(df)


if __name__ == '__main__':
    demo()
