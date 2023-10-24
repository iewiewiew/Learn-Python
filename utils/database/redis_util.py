# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 9:35
@description  Python连接Redis
"""

import redis

import redis


class RedisUtils:
    def __init__(self, host, port, db, password=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = redis.Redis(
            host=self.host,
            port=self.port,
            db=self.db,
            password=self.password
        )

    def get(self, key):
        return self.connection.get(key)

    def get_all_keys(self):
        return self.connection.keys()

    def set(self, key, value):
        self.connection.set(key, value)

    def delete(self, key):
        self.connection.delete(key)

    def flushdb(self):
        self.connection.flushdb()

    def flushall(self):
        self.connection.flushall()

    def disconnect(self):
        self.connection.close()


def python_redis():
    # conn = redis.Redis(host="127.0.0.1", port=6379, password="root", decode_responses=True)
    # print(conn.ping)
    # print(conn.keys())

    pool = redis.ConnectionPool(host="127.0.0.1", port=6379, password="root")
    conn = redis.Redis(connection_pool=pool)
    print(conn.ping())
    print(conn.keys())

    conn.set("keytest", "i am value")
    print("keytest值：", conn.get("keytest"))
    print("keytest值：", conn["keytest"])


if __name__ == '__main__':
    """创建实例"""
    redis_utils = RedisUtils(host='localhost', port=6379, db=0)
    redis_utils.connect()

    """设置 Key"""
    # redis_utils.set('mykey', 'myvalue')

    """查询 Key"""
    # value = redis_utils.get('mykey')
    # print(value)  # 输出: b'myvalue'

    """查询所有 Key"""
    value = redis_utils.get_all_keys()
    print(value)
    keys = [key.decode() for key in redis_utils.get_all_keys()]
    print(keys)

    """删除 Key"""
    # redis_utils.delete('mykey')

    """清除单个缓存"""
    redis_utils.flushdb()

    """清除所有缓存"""
    redis_utils.flushall()

    """关闭连接"""
    redis_utils.disconnect()
