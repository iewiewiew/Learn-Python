# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/4 0:33
@description  句柄，获取窗口

元素有属性，浏览器的窗口其实也有属性的，浏览器窗口的属性用句柄（handle）来识别；
获取当前页面的句柄：browser.current_window_handle；
获取所有窗口句柄：brows.window_handles。
"""

from selenium import webdriver
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    # 获取当前窗口句柄
    print(driver.current_window_handle)

    # 获取所有窗口句柄
    print(driver.window_handles)

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
