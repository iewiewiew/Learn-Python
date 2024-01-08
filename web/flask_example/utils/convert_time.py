# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/22 14:15
@description  注：未调试成功

npm install axios moment
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route('/convert', methods=['POST'])
def convert_time():
    data = request.get_json()
    timestamp = data['timestamp']
    timestamp_type = data['timestamp_type']
    if timestamp_type == 'seconds':
        converted_time = datetime.fromtimestamp(int(timestamp))
    elif timestamp_type == 'milliseconds':
        converted_time = datetime.fromtimestamp(int(timestamp) / 100)
    else:
        return jsonify({'error': 'Invalid timestamp type'})
    return jsonify({'result': converted_time.strftime('%Y-%m-%d %H:%M:%S')})


if __name__ == '__main__':
    app.run(debug=True)