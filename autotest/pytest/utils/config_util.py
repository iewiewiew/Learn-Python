# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/3/28 21:51
@description  读取 yaml 文件
"""

import yaml


def read_yaml(file_path, validate=False):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file) or {}
        if validate:
            data = yaml.safe_load(file, validate=True)
        return data


if __name__ == '__main__':
    file_path = '../config/config-git.yml'
    data = read_yaml(file_path)
    print(data['param']['repo_dir'])
