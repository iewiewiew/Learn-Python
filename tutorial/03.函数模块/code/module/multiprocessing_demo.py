# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/5/15 11:30
@description  @multiprocessing 多线程处理
"""


import multiprocessing
import os
import time


def worker():
    print("Worker started")
    time.sleep(5)
    print("Worker finished")


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker)
    p.start()
    print("Main process waiting for worker to finish")
    p.join()
    print("Main process printing result")
    # os.system("pause")
