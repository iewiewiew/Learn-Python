# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/25 9:03
@description  ocr识别验证码
"""

from PIL import Image
from ddddocr import DdddOcr
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def demo():
    """
    体验管理员: admin 
    密码: shopxo
    https://d2.shopxo.vip/admin.php?s=admin/logininfo.html
    """

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://d2.shopxo.vip/admin.php?s=admin/logininfo.html')

    driver.find_element(By.XPATH, "//input[@name='accounts']").send_keys('admin')
    driver.find_element(By.XPATH, "//input[@name='pwd']").send_keys('shopxo')
    files = driver.find_elements(By.XPATH, "//span[@class='am-input-group-btn']")[1]
    sleep(2)
    # 保存截图
    driver.save_screenshot('../files/old_verify.png')
    # 获取位置
    location = files.location
    print(location)
    # 获取大小
    files_size = files.size
    print(files_size)
    # 确定所需要的图片大小
    rangle = (int(location['x'] - 5), int(location['y'] - 5), int(location['x'] + files_size['width'] + 11),
              int(location['y'] + files_size['height'] + 7))
    # 打开之前截图图片
    image = Image.open('../files/old_verify.png')
    # 开始裁剪
    image1 = image.crop(rangle)
    # 保存裁剪后的截图
    image1.save('../files/verify.png')
    # 实例化类方法
    ocr = DdddOcr()
    # 打开图片，二进制形式
    file = open(r'../files/verify.png', 'rb')
    # 读取图片
    img = file.read()
    # 识别图片验证码
    result = ocr.classification(img)
    print(result)

    driver.find_element(By.XPATH, "//input[@name='verify']").send_keys(result)
    driver.find_element(By.XPATH, "//*[text()='登录']").click()


def ocr_demo():
    # 实例化方法
    ocr = DdddOcr()
    # 打开图片
    file = open(r'../files/verify.png', 'rb')
    # 读取图片
    img = file.read()
    # 识别图片
    result = ocr.classification(img)
    # 打印内容
    print(result)


if __name__ == '__main__':
    demo()
    # ocr_demo()
