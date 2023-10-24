# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 9:29
@description  检测服务进程是否存在
"""

import os


def check_service():
    process = "./check_service.lock"
    # 将进程信息写入lock文件 Chrome
    os.system("ps -ef|grep Python |grep -v grep >%s" % process)

    # 判断文件大小，当tomcat没有运行时上一步写入lock的内容为空
    if not (os.path.getsize(process)):
        # 执行start.sh脚本启动服务
        # os.system("/app/demo/bin/start.sh")
        print("服务不存在")
    else:
        print("服务存在")


if __name__ == '__main__':
    check_service()
