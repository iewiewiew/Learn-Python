# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/8 22:44
@description  Airtest是一个跨平台的UI自动化框架，适用于游戏和App。
pip install -U airtest
Airtest官网：https://airtest.netease.com/
Airtest文档：https://airtest.readthedocs.io/zh_CN/latest/
"""

from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome

def demo():
    driver = WebChrome()
    driver.implicitly_wait(20)

    driver.get("http:www.baidu.com")

    auto_setup(__file__)
    driver.get("http:www.baidu.com")


if __name__ == '__main__':
    demo()


# 通过ADB连接本地Android设备
# connect_device("Android:///")
# install("path/to/your/apk")
# start_app("package_name_of_your_apk")
# touch("image_of_a_button.png")
# swipe("slide_start.png", "slide_end.png")
# assert_exists("success.png")
# keyevent("BACK")
# home()
# uninstall("package_name_of_your_apk")