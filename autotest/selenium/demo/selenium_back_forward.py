# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 11:03
@description  前进后退打开不同网页
"""

from selenium import webdriver
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    # 访问微博首页
    first_url = "http://www.weibo.com"
    print("now access %s" % (first_url))
    driver.get(first_url)
    time.sleep(5)

    # 访问百度页面
    second_url = "http://www.baidu.com"
    print("now access %s" % (second_url))
    driver.get(second_url)
    time.sleep(5)

    # 后退到微博首页
    print("back to %s" % (first_url))
    driver.back()
    time.sleep(5)

    # 前进到百度页面
    print("forward to %s" % (second_url))
    driver.forward()

    # 刷新
    driver.refresh()

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
