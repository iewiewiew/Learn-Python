# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/17 11:17
@description  Flask 示例
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Flask"


if __name__ == '__main__':
    app.run(debug=True)
