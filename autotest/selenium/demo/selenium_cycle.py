# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 11:03
@description  获取多个元素
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# todo 未运行成功
def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    driver.find_element(By.ID, "kw").send_keys("selenium")
    driver.find_element(By.ID, "su").click()

    # 1.定位一组元素
    elements = driver.find_elements(By.XPATH, '//div/h3/a')
    print("1.定位一组元素")
    print(type(elements))

    # 2.循环遍历出每一条搜索结果的标题
    for t in elements:
        print("2.循环遍历出每一条搜索结果的标题")
        print(t.text)
        element = driver.find_element(By.LINK_TEXT, t.text)
        print(element)
        element.click()

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
