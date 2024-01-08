# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/22 11:15
@description  消息闪现
"""

from flask import Flask, request, url_for, redirect, render_template, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index11_flask_flush.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            flash('登录成功！', 'info')
            return redirect(url_for('index'))
        else:
            error = 'login failed'
    return render_template('index11_flask_flush_login_demo.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
