# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/5 16:24
@description  下载文件
"""

import os
from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


@app.route('/')
def show_files():
    # files = os.listdir(directory)  # 获取目录及文件文件

    files = sorted(get_files(directory))  # 获取指定目录的文件

    # files = sorted(get_all_files(directory))   # 获取指定目录及子目录的所有文件

    return render_template('download.html', files=files)


@app.route('/download/<path:filepath>')
def download_file(filepath):
    return send_from_directory(directory, filepath, as_attachment=True)


def get_files(directory):
    """获取指定目录的文件"""

    files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(file_path) and not filename.startswith('.'):
            files.append(filename)
    return files


def get_all_files(directory):
    """获取指定目录及子目录的所有文件"""

    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, directory)
            files.append(relative_path)
    return files


if __name__ == '__main__':
    directory = '/Users/menghuawei/PycharmProjects/Learn-Python/.gitee/tmp'  # 本地路径
    app.run(host='0.0.0.0', port=8888)
