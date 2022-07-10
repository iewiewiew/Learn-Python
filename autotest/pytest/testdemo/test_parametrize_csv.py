#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @pytest.mark.parametrize：csv参数化
"""

import json
import pytest
import requests
import csv
from utils import get_project_root


def readCsv():
    data = list()
    fliePath = get_project_root("Learn-Python") + "\\autotest\\pytest\\testdata\\csv_data.csv"
    with open(fliePath, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            data.append(item)
    return data


@pytest.mark.parametrize('data', readCsv())
def test_csv(data):
    response = requests.post(url=data[0], json=json.loads(data[1]))
    assert response.json() == json.loads(data[2])


if __name__ == '__main__':
    pytest.main()
