# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/27 17:03
@description  MySQL 相关操作
"""


import pymysql
from pymysql.cursors import DictCursor


class DoMysql:
    """
    sql数据库查询类
    """

    def __init__(self, db_config: dict):
        # 创建连接
        engine = db_config.pop('engine', 'mysql')
        if engine.lower() == 'mysql':
            self.conn = pymysql.connect(**db_config)
        elif engine.lower() == 'oracle':
            pass

    def __execute(self, sql, action, res_type='t', *args):
        """
        :param sql:
        :param action: 字符串，指定执行cursor对应的方法
        :param res_type: 返回数据类型
        :param args:
        :return:
        """
        if res_type == 't':
            cursor = self.conn.cursor()
        else:
            cursor = self.conn.cursor(DictCursor)
        try:
            cursor.execute(sql)
            return getattr(cursor, action)(*args)
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def get_one(self, sql, res_type='t'):
        """
        获取一条数据
        :param sql:
        :param res_type: 返回数据的类型，默认为t表示以元组返回，'d'表示以字典的形式返回
        :return: 元组/字典
        """
        # 数据库若断开即重连
        self.reConnect()
        return self.__execute(sql, 'fetchone', res_type)

    def get_many(self, sql, size, res_type='t'):
        # 数据库若断开即重连
        self.reConnect()
        return self.__execute(sql, 'fetchmany', res_type, size)

    def get_all(self, sql, res_type='t'):
        # 数据库若断开即重连
        self.reConnect()
        return self.__execute(sql, 'fetchall', res_type)

    def exist(self, sql):
        if self.get_one(sql):
            return True
        else:
            return False

    def reConnect(self):
        """
        重连机制
        :@return
        """
        try:
            self.conn.ping()
        except:
            self.conn()

    def __del__(self):
        """
        对象销毁的时候自动会被调用
        :return:
        """
        self.conn.close()


if __name__ == '__main__':
    db = {
        'engine': 'mysql',
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'root',
        'port': 3306,
        'db': 'mysql',
        'charset': 'utf8'
    }
    db = DoMysql(db)
    sql = 'select * from dbname.t_table_info limit 2'
    res = db.get_one(sql)
    # res = db.get_many(sql, size=5)
    print(res)