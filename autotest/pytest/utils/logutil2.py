# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/16 19:15
@description
"""

import logging
import time
import os
from utils import get_project_root


def get_log(logger_name):
    """
    :param logger_name: 日志名称
    :return: 返回logger handle
    """
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 获取本地时间，转换为设置的格式
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))

    # 设置所有日志和错误日志的存放路径
    all_log_path = get_project_root("Learn-Python") + "\\autotest\\pytest\\logs\\"
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)

    error_log_path = get_project_root("Learn-Python") + "\\autotest\\pytest\\logs\\"
    if not os.path.exists(error_log_path):
        os.makedirs(error_log_path)

    # 设置日志文件名
    all_log_name = all_log_path + rq + '.log'
    error_log_name = error_log_path + rq + '.log'

    if not logger.handlers:
        # 创建一个handler写入所有日志
        fh = logging.FileHandler(all_log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 创建一个handler写入错误日志
        eh = logging.FileHandler(error_log_name, encoding='utf-8')
        eh.setLevel(logging.ERROR)

        # 创建一个handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        all_log_formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s - %(levelname)s - %(lineno)s - %(message)s')
        # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        error_log_formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s - %(levelname)s - %(lineno)s - %(message)s')
        # 将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(eh)
        logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    logger = get_log(os.path.split(__file__)[-1])
    logger.info("12345")
    logger.debug("12345")
    logger.warning("12345")
    logger.error("12345")
