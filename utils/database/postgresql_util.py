# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/24 14:40
@description  Postgresql 工具类
"""

import psycopg2


class PostgresUtils:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_update(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows

    def disconnect(self):
        self.connection.close()


if __name__ == '__main__':
    postgres_utils = PostgresUtils(
        host='127.0.0.1',
        port=5432,
        database='dbdemo',
        user='postgres',
        password='postgres'
    )
    postgres_utils.connect()

    """执行查询"""
    query = "SELECT * FROM tabledemo"
    result = postgres_utils.execute_query(query)
    print(result)

    """执行更新"""
    update_query = "UPDATE tabledemo SET name = %s WHERE id = %s"
    params = ('new_value', 1)
    affected_rows = postgres_utils.execute_update(update_query, params)
    print(f"Affected rows: {affected_rows}")

    postgres_utils.disconnect()
