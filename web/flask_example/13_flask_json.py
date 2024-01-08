# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/22 15:58
@description  返回 JSON
"""

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        page_id = request.args.get('page_id')
        if user_id is None or page_id is None:
            return make_response(jsonify({"code": 2000, "msg": "user_id or page_id is none!"}), 200)
        return make_response(jsonify({"code": 0, "msg": "Success"}), 200)
    else:
        return make_response(jsonify({"code": 2001, "msg": "Invalid request method"}), 405)


if __name__ == '__main__':
    app.run(debug=True)

    """
    测试地址：http://127.0.0.1:5000/?user_id=1&page_id=2
    """
