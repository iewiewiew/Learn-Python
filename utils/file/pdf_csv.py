# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/27 17:14
@description  注：未实践成功

pip install tabula-py
"""

import tabula


def demo():
    filename = '/Users/menghuawei/PycharmProjects/Learn-Python/file/pdf/csvdemo.pdf'

    # df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')
    df = tabula.read_pdf(filename, encoding='utf-8', pages='1')

    df.to_csv('/Users/menghuawei/PycharmProjects/Learn-Python/file/csv/csvdemo_output.csv')


if __name__ == '__main__':
    demo()
