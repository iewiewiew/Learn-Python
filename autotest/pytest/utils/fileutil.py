#!/usr/bin/python3
# coding:utf-8

"""
@author      weimenghua
@time        2022/2/12 11:51
@description 读取文件
"""

import csv
import xlrd
import json

from utils.path_util import get_project_root


def readCsv():
    data = list()
    fliePath = get_project_root("Learn-Python") + "\\autotest\\pytest\\testdata\\csv_data.csv"
    with open(fliePath, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            data.append(item)
        print(data)


def readExcel():
    data = list()
    fliePath = get_project_root("Learn-Python") + "\\autotest\\pytest\\testdata\\excel_data.xls"
    book = xlrd.open_workbook(fliePath)
    sheet = book.sheet_by_index(0)
    for item in range(1, sheet.nrows):
        data.append(sheet.row_values(item))
    print(data)


def readJson():
    fliePath = get_project_root("Learn-Python") + "\\autotest\\pytest\\testdata\\json_data.json"
    file = json.load(open(fliePath, 'r', encoding="utf-8"))
    item = file['item']
    request = file['item'][0]['request']
    response = file['item'][0]['response']
    print(response)


if __name__ == '__main__':
    readCsv()
    readJson()
    readExcel()
