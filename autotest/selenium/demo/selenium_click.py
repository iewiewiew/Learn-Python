# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/22 8:29
@description  鼠标操作

ActionChains 类提供的鼠标操作的常用方法, perform() 执行所有 ActionChains 中存储的行为,
1、context_click() 右击
2、double_click() 双击
3、drag_and_drop() 拖动
4、move_to_element() 悬停
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    driver.find_element(By.ID, "kw").send_keys("点击右键")
    time.sleep(1)

    # 1、context_click() 右击
    # 调用 ActionChains()方法，在使用将浏览器驱动 driver 作为参数传入。
    # context_click()方法用于模拟鼠标右键事件，在调用时需要传入右键的元素。
    # 执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
    right_click = driver.find_element(By.ID, "kw")
    ActionChains(driver).context_click(right_click).perform()

    # 2、double_click() 双击
    dubbo_click = driver.find_element(By.ID, "kw")
    ActionChains(driver).double_click(dubbo_click).perform()

    # 3、drag_and_drop() 拖动
    # 定位元素的源位置
    # element = driver.find_element(By.ID, "xxx")
    # 定位元素要移动到的目标位置
    # target = driver.find_element(By.ID, "xxx")
    # 执行元素的拖放操作
    # ActionChains(driver).drag_and_drop(element, target).perform()

    # 4、move_to_element() 悬停
    above = driver.find_element(By.LINK_TEXT, u'设置')
    ActionChains(driver).move_to_element(above).perform()

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
