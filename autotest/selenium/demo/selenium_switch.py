# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/23 10:40
@description  多窗口切换
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(3)

    # 先通过xpth定位到iframe
    # xf = driver.find_element(By.XPATH, '//*[@id="x-URS-iframe"]')

    # 再将定位对象传给switch_to_frame()方法
    # driver.switch_to_frame(xf)

    # driver.switch_to_default_content()  # 返回父frame

    # 1.获得百度搜索窗口句柄
    sreach_windows = driver.current_window_handle

    print(driver.current_window_handle)
    driver.find_element(By.LINK_TEXT, u'登录').click()

    print(driver.current_window_handle)
    driver.switch_to.alert
    driver.find_element(By.XPATH, "//*[@id='TANGRAM__PSP_11__regLink']").click()

    print(driver.window_handles)

    # 1.获得当前所有打开的窗口的句柄
    all_handles = driver.window_handles

    # 3.进入注册窗口
    for handle in all_handles:
        if handle != sreach_windows:
            driver.switch_to.window(handle)
        print('跳转到注册窗口')
        driver.find_element(By.CLASS_NAME, "account").send_keys('123456789')
        driver.find_element(By.CLASS_NAME, 'password').send_keys('123456789')
        time.sleep(2)

    driver.quit()


if __name__ == '__main__':
    demo()