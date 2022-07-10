# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/9 20:13
@description  测试WebSocket接口

pip install websocket、pip install websocket-client
建立WebSocket连接：ws://127.0.0.1:9999/websocket/demo。
发起WebSocket请求：ws://127.0.0.1:9999/wbtest/sendMsg/test_websocket。
"""

import websocket
from websocket import create_connection
from threading import Thread
import time


# on_message用来接受消息，server发送的所有消息都可以用on_message来收取
def on_message(ws, message):
    print(message)


# on_error用来处理错误异常，捕捉socket的程序通信的问题
def on_error(ws, error):
    print(error)


# on_close用来关闭socket连接的
def on_close(ws):
    print("### closed ###")


# on_open用来保持连接的
def on_open(ws):
    def run(*args):
        for i in range(3):
            ws.send("Hello %d" % i)
            time.sleep(1)

        time.sleep(1)
        ws.close()
        print("关闭连接")

    Thread(target=run).start()


def demo1():
    websocket.enableTrace(True)
    host = "ws://127.0.0.1:9999/websocket/demo"
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    # run_forever()保持长连接
    ws.run_forever()


def demo2():
    host = "ws://127.0.0.1:9999/websocket/demo"
    ws = create_connection(host)
    print("发送 'Hello, World'...")
    ws.send("Hello, World")
    result = ws.recv()
    print("接收 '%s'" % result)
    ws.close()  # 关闭socket连接
    print("关闭连接")


if __name__ == "__main__":
    demo2()
