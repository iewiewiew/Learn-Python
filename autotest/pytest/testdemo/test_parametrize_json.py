#!/usr/bin/env python
# !coding:utf-8

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @pytest.mark.parametrize：json参数化
"""

import pytest
import requests
import json
from utils import get_project_root


def readJson():
    fliePath = get_project_root("Learn-Python") + "\\autotest\\pytest\\testdata\\json_data.json"
    return json.load(open(fliePath, 'r', encoding="utf-8"))['item']


@pytest.mark.parametrize('data', readJson())
def test_json(data):
    response = requests.post(url=data['request']['url'], json=data['request']['body'])
    assert str(response.json()).lower() == data['response']


if __name__ == '__main__':
    pytest.main()
