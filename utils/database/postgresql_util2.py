# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/24 15:39
@description  Postgresql 工具类
"""

import psycopg2


class PostgresTool:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def execute(self, sql, params=None):
        try:
            self.cur.execute(sql, params)
            self.conn.commit()
            return self.cur.fetchall()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def insert(self, table, columns, values):
        try:
            sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
            self.cur.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def update(self, table, set_values, where):
        try:
            set_str = ', '.join([f"{k} = %s" for k in set_values.keys()])
            where_str = ' AND '.join([f"{k} = %s" for k in where.keys()])
            values = list(set_values.values()) + list(where.values())
            sql = f"UPDATE {table} SET {set_str} WHERE {where_str}"
            self.cur.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def delete(self, table, where):
        try:
            where_str = ' AND '.join([f"{k} = %s" for k in where.keys()])
            values = list(where.values())
            sql = f"DELETE FROM {table} WHERE {where_str}"
            self.cur.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def select(self, table, columns=None, where=None):
        try:
            col_str = '*'
            if columns:
                col_str = ', '.join(columns)
            where_str = ''
            values = []
            if where:
                where_str = ' WHERE ' + ' AND '.join([f"{k} = %s" for k in where.keys()])
                values = list(where.values())
            sql = f"SELECT {col_str} FROM {table} {where_str}"
            self.cur.execute(sql, values)
            return self.cur.fetchall()
        except Exception as e:
            print(e)
            self.conn.rollback()


if __name__ == '__main__':
    # 创建工具类实例
    tool = PostgresTool(dbname='dbdemo', user='postgres', password='postgres', host='127.0.0.1', port='5432')

    # 连接数据库
    tool.connect()

    # 插入数据
    tool.insert('tabledemo', ['name', 'age'], ['张三', 20])

    # 更新数据
    tool.update('tabledemo', {'age': 21}, {'name': '张三'})

    # 删除数据
    tool.delete('tabledemo', {'name': '张三'})

    # 查询数据
    result = tool.select('tabledemo', ['name', 'age'], {'age': 20})
    print(result)

    # 关闭数据库连接
    tool.close()
