# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/19 15:34
@description
"""

from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__, template_folder='template')


@app.errorhandler(404)
def error(e):
    if request.method == 'GET':
        response = requests.get("http://test/" + request.path)
        return response.text
    elif request.method == 'POST':
        response = requests.post("http://test/" + request.path, data=request.data)
        return response.text
    return render_template("404.json")


if __name__ == "__main__":
    app.run(debug=True)
