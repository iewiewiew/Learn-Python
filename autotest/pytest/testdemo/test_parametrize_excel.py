#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @pytest.mark.parametrize：excel参数化
"""

import pytest
import requests
import xlrd
import json
from utils import get_project_root


def readExcel():
    data = list()
    fliePath = get_project_root("Learn-Python") + "\\autotest\\pytest\\testdata\\excel_data.xls"
    book = xlrd.open_workbook(fliePath)
    sheet = book.sheet_by_index(0)
    for item in range(1, sheet.nrows):
        data.append(sheet.row_values(item))
    return data


@pytest.mark.parametrize('data', readExcel())
def test_excel(data):
    r = requests.post(url=data[0], json=json.loads(data[1]))
    assert r.json() == json.loads(data[2])


if __name__ == '__main__':
    pytest.main()