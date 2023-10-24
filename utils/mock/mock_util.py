# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/24 16:07
@description  Mock 请求
"""
import json

from flask import Flask, jsonify, request
from faker import Faker

from utils.database.mysql_util import Database

app = Flask(__name__)
fake = Faker()


@app.route('/get', methods=['GET'])
def get_test():
    return '{"name": "jim","age": 16,"gender": 1,"isStudent": true}'


@app.route('/post', methods=['POST'])
def post_test():
    data = request.get_json()
    print(data)
    response = {}
    for key, value in data.items():
        if value == 'name':
            response[key] = fake.name()
        elif value == 'address':
            response[key] = fake.address()
        elif value == 'email':
            response[key] = fake.email()
        # 添加其他需要的字段类型和对应的生成方式
        else:
            response[key] = None
    return jsonify(response)


@app.route('/test', methods=['GET', 'POST'])
def demo():
    if request.method == 'GET':
        return 'Is a get request!'
    elif request.method == 'POST':
        return 'Is a post request'


@app.route('/get_sql', methods=['GET'])
def get_sql():
    db = Database(host='localhost', port=3306, user='root', password='root', database='dbname')
    db.connect()
    query = "select * from dbname.t_table_info"
    result = db.execute_query(query)
    resp = json.dumps(result, ensure_ascii=False)
    return resp  # @todo 返回 null


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)  # 端口默认 5000

    """
    POST http://127.0.0.1:5000/post
    {
        "name": "name",
        "address": "address",
        "email": "email"
    }
    """
