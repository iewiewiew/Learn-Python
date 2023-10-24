# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/25 10:00
@description  json 转换为 sql
"""

import json


def json_to_sql(json_data, table_name):
    # 解析 JSON 数据
    data = json.loads(json_data)

    # 获取字段和值
    columns = list(data.keys())
    values = list(data.values())

    # 构建 SQL 插入语句
    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

    return sql, values


def json_to_sql2(json_data, table_name):
    # 解析 JSON 数据
    data = json.loads(json_data)

    # 获取字段和值
    columns = list(data.keys())
    values = list(data.values())

    # 构建 SQL 插入语句
    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(map(format_value, values))})"

    return sql


def format_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, (int, float)):
        return str(value)
    elif value is None:
        return 'NULL'
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")


if __name__ == '__main__':
    json_data = '{"name": "John Doe", "age": 25, "city": "New York"}'
    table_name = "users"

    sql, values = json_to_sql(json_data, table_name)
    print(sql)  # INSERT INTO users (name, age, city) VALUES (%s, %s, %s)
    print(values)  # ['John Doe', 25, 'New York']

    sql2 = json_to_sql2(json_data, table_name)
    print(sql2)  # INSERT INTO users (name, age, city) VALUES ('John Doe', 25, 'New York')