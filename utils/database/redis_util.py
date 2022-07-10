# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 9:35
@description  Python连接Redis
"""

import redis


# 启动Redis：D: && cd D:\software\redis-2.8.9\ && redis-server.exe redis.windows.conf
def python_redis1():
    conn = redis.Redis(host="127.0.0.1", port=6379, password="root", decode_responses=True)
    print(conn.ping)
    print(conn.keys())


def python_redis2():
    pool = redis.ConnectionPool(host="127.0.0.1", port=6379, password="root")
    conn = redis.Redis(connection_pool=pool)
    print(conn.ping())
    print(conn.keys())


def python_redis3():
    pool = redis.ConnectionPool(host="127.0.0.1", port=6379, password="root")
    conn = redis.Redis(connection_pool=pool)
    conn.set("keytest", "i am value")
    print("keytest值：", conn.get("keytest"))
    print("keytest值：", conn["keytest"])


if __name__ == '__main__':
    python_redis1()
    python_redis2()
    python_redis3()