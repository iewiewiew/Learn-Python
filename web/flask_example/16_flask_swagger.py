# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/26 10:04
@description
"""

from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    """
    A simple hello world API.
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: The name parameter in the URL path.
    responses:
      200:
        description: A greeting message.
        schema:
          type: string
    """
    return f"Hello, {name}!"


if __name__ == '__main__':
    app.run(debug=True)

    """
    http://127.0.0.1:5000/hello/wei
    http://127.0.0.1:5000/apidocs/
    """
