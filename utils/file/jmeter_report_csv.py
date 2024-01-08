# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/4/7 16:47
@description
"""
import openpyxl
from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route('/')
def display_excel():
    base_path = '/Users/menghuawei/PycharmProjects/my-project/Learn-Python/.gitee/tmp/20240406221159/'
    excel_file = base_path + '负载测试报告_20240407_20240406221159.xlsx'
    data = []

    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook.active

    for row in worksheet.iter_rows(values_only=True):
        data.append(row)

    return render_template('display.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
