# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/11 23:52
@description  pdf 工具类
"""

from PyPDF2 import PdfFileReader


def read_pdf():
    with open('../../../files/word2.pdf', 'rb') as f:
        reader = PdfFileReader(f, strict=False)
        print("页数：", reader.numPages)
        if reader.isEncrypted:
            reader.decrypt('')
        current_page = reader.getPage(0)
        print("当前页信息：", current_page)
        print("这是啥：", current_page.extractText())


if __name__ == '__main__':
    read_pdf()
