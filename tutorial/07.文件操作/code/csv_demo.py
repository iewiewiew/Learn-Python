# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author      weimenghua
@time        2020/12/10 21:42
@description 读写 csv
"""

import pandas
from utils import get_file_path


def wirte_csv():
    # data 为需要写入的数据,使用字典格式，key 为列名，values 为每一行的内容
    data = {
        "name": "wei",    # string 直接写入即可
        "age": [123],     # int 类型需要使用[]括起来
        "sex": "girl",
        "remark": "其它信息"
    }

    dataCSV = pandas.DataFrame(data)

    """
    mode = "a"，追加模式，如果不使用这个模式，会把前面的内容覆盖。
    header = False：不写入头部信息，即字典中的 key 值不写入。
    encoding = "GBK"：编码格式为 GBK，即中文编码，默认为 utf-8，如果数据有中文时则可能会报错(encoding 为 GBK 格式的时候中文会乱码)
    """
    dataCSV.to_csv(get_file_path() + "csvdemo.csv", index=False, mode="w", header=False, encoding="UTF-8")

    print("写入 csv 完成")


if __name__ == '__main__':
    wirte_csv()
