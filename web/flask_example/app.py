# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/23 14:29
@description
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask'


if __name__ == '__main__':
    app.run(debug=True)