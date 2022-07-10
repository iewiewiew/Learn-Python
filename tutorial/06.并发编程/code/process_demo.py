# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/11 17:18
@description  多线程
"""

from multiprocessing import Process
from os import getpid
from random import randint
from threading import Thread
from time import time, sleep


# 下载任务
def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s 下载完成! 耗费了%d 秒' % (filename, time_to_download))


# 多线程下载任务
def download_task_test():
    start = time()

    p1 = Process(target=download_task, args=('demo1.pdf',))
    p1.start()

    p2 = Process(target=download_task, args=('demo2.pdf',))
    p2.start()

    p1.join()
    p2.join()

    end = time()

    print('总共耗费了%.2f 秒.' % (end - start))


# 下载任务 继承 Thread
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s 下载完成! 耗费了%d 秒' % (self._filename, time_to_download))


# 多线程下载任务
def download_task_test1():
    start = time()

    t1 = DownloadTask('demo1.pdf')
    t1.start()

    t2 = DownloadTask('demo2.pdf')
    t2.start()

    t1.join()
    t2.join()

    end = time()
    print('总共耗费了%.2f 秒.' % (end - start) + '/n')


"""
线程间通信（共享数据）非常简单因为可以共享同一个进程的内存
进程间通信（共享数据）比较麻烦因为操作系统会保护分配给进程的内存
要实现多进程间的通信通常可以用系统管道、套接字、三方服务来实现
multiprocessing.Queue
守护线程 - daemon thread
守护进程 - firewalld / httpd / mysqld
在系统停机的时候不保留的进程 - 不会因为进程还没有执行结束而阻碍系统停止
"""


def output(content):
    while True:
        print(content, end='')


def thread_test():
    Thread(target=output, args=('Ping',), daemon=True).start()
    Thread(target=output, args=('Pong',), daemon=True).start()
    sleep(5)
    print('bye!')


if __name__ == '__main__':
    # download_task_test()
    download_task_test1()
    # thread_test()
