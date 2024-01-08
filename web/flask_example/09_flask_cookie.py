# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/21 10:54
@description  Cookie 注：未调试成功
"""

import time
from flask import Flask, request, session, make_response

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            session['username'] = request.form['username']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            return 'No such user!'
    elif request.method == 'GET':
        if request.form['username'] == 'admin':
            session['username'] = request.form['username']
        else:
            return 'No such user!'


if __name__ == '__main__':
    app.run(debug=True)

    """
    curl http://127.0.0.1:5000/login?username=admin
    """
