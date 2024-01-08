# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/23 11:19
@description  Blueprint 用于管理 Flask 应用的路由和视图函数
"""

from flask import Flask, Blueprint, jsonify

# 创建 Flask 应用
app = Flask(__name__)

# 创建一个 Blueprint 对象
example_blueprint = Blueprint('example', __name__)


# 定义基于 Blueprint 的路由和视图函数
@example_blueprint.route('/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})


@example_blueprint.route('/greet/<name>')
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})


# 注册 Blueprint
app.register_blueprint(example_blueprint, url_prefix='/example')

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)

    """
    http://127.0.0.1:5000/example/hello
    http://127.0.0.1:5000/example/greet/haha
    """
