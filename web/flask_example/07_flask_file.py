# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/19 10:32
@description  文件上传
"""

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save('/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/' + secure_filename(f.filename))
        return 'file uploaded successfully'
    else:
        return render_template('index7_flask_file.html')


if __name__ == '__main__':
    app.run(debug=True)
