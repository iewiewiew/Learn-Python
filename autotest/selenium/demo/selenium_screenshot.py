# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/21 22:51
@description  窗口截图
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import get_project_root
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    try:
        driver.find_element(By.ID, 'kw').send_key('selenium')
        driver.find_element(By.ID, 'su').click()
    except:
        fliePath = get_project_root("Learn-Python") + "\\autotest\\selenium\\files\\screenshot_error.png"
        driver.get_screenshot_as_file(fliePath)

        time.sleep(3)
        driver.quit()


if __name__ == '__main__':
    demo()
