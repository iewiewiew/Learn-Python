# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/4 0:37
@description  显隐式等待

WebDriverWait类提供了显式等待和隐式等待。
WebDriverWait() 显式等待的等待时间是固定的，固定了10s就必须等待10s。显式等待仅适用于特定实例, 用于中止当前执行, 直到满足特定条件的元素出现为止（在允许的时间内）。
implicitly_wait() 隐式等待的等待时间是个范围，例如最大10s，那么如果在3s的时候程序达到预期的结果，那么就不在继续后面的7秒，直接进入下一步操作，而如果超出10s还没有相应，程序就会报出相应的错误。
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.baidu.com')

    # 隐式等待最大5秒
    driver.implicitly_wait(5)

    # 显示等待最大5秒
    # WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
    # driver：浏览器驱动
    # timeout：最长超时时间，默认以秒为单位
    # poll_frequency：检测的时隔步长(在2中表示调用until或until_not中方法的间隔时间），默认是0.5s
    # ignored_exceptions: 超时后的抛出的异常信息，默认抛出NoSuchException信息。
    element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'kw')))
    element.send_keys('selenium')

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
