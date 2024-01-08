# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/17 11:17
@description  Flask 示例
"""

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return "Hello hello"


@app.route('/test')
def hello2():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


def hello3():
    return "Hello Flask"


@app.route('/redirect')
def index():
    redirect('/test', 301)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8888)

    # app.add_url_rule('/hello3', view_func=hello3)  # 注：未调试成功
