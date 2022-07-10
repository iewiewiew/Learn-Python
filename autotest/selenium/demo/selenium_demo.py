# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 11:03
@description  selenium demo
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    driver.find_element(By.ID, "kw").send_keys("selenium")
    driver.find_element(By.ID, "su").click()

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
