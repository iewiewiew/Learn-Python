# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/23 10:58
@description  下拉选择

1、select_by_value(“选择值”)	        select标签的value属性的值
2、select_by_index(“索引值”)	        下拉框的索引
3、select_by_visible_testx(“文本值”)	下拉框的文本值
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(3)

    driver.find_element(By.ID, "kw").send_keys("selenium")
    driver.find_element(By.ID, "su").click()

    sel = driver.find_element(By.XPATH, "//*select[@id='nr']")
    Select(sel).select_by_value('2')  # 显示2条

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
