# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/23 10:29
@description  selenium 基本操作
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(3)

    driver.set_window_size(1000, 600)

    print(driver.title)
    print(driver.current_url)
    print(driver.get_window_size())
    print(driver.page_source)

    driver.find_element(By.ID, "kw").send_keys("selenium2")
    time.sleep(3)

    driver.find_element(By.ID, "kw").clear()  # 清除内容

    driver.find_element(By.ID, "kw").send_keys("selenium")

    driver.find_element(By.ID, "kw").submit()  # 回车

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
