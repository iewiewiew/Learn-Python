# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/13 16:23
@description  MySQL 相关操作
"""
import random
import pymysql

rand = random.randint(100, 200)


class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        # print(result)
        for row in result:
            print(row)

    def execute_update(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        affected_rows = self.cursor.rowcount
        print(f"Affected rows: {affected_rows}")

    def insert_data(self, table, data):
        columns = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()


if __name__ == '__main__':
    """创建 Database 实例"""
    db = Database(host='localhost', port=3306, user='root', password='root', database='dbname')

    """连接到数据库"""
    db.connect()

    """执行查询语句"""
    # query = "SELECT * FROM dbname.`t_table_info`"
    # query = "SHOW DATABASES"
    query = "SHOW TABLES"
    # query = "SHOW BINARY LOGS;"
    # query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'oauth_applications'"
    # query = "select * from gitlabhq_production.oauth_applications where id in (888, 1281, 1286)"
    db.execute_query(query)

    """执行更新语句"""
    # update_query = "UPDATE dbname.`t_table_info` SET `name` = 'new_value' WHERE id = 1"
    # db.execute_update(update_query)

    """插入数据"""
    # table = 't_table_info'
    # data = {'id': rand, 'name': 'python', 'age': 18}
    # inserted_id = db.insert_data(table, data)
    # print(f"Inserted row ID: {inserted_id}")

    """断开数据库连接"""
    db.disconnect()
