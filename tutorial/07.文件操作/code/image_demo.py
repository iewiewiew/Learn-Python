# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/25 08:34
@description  创建图片

查看本地安装了的字体： ls /Library/Fonts/ Arial Unicode.ttf
"""

import os
import time
from PIL import Image, ImageDraw, ImageFont


def image_demo():
    img = Image.open('../../../files/桌面背景.png')
    print(img.size)
    print(img.format)
    print(img.mode)
    print(img.format_description)

    # 保存图片
    img.save('../../files/桌面背景2.png')

    # 裁剪图片
    img2 = Image.open('../../../files/桌面背景2.png')
    rect = 80, 20, 310, 360
    img2.crop(rect).show()

    # 生成缩略图
    img3 = Image.open('../../../files/桌面背景2.png')
    size = 128, 128
    img3.thumbnail(size)
    img3.show()


def create_image():
    if not os.path.exists("../../../files/img"):
        os.makedirs("../../../files/img")

    for i in range(1, 6):
        img = Image.new('RGB', (800, 300), color='white')
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype('Arial Unicode.ttf', 36)
        d.text((100, 150), "PNG_" + str(i) + "_" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))),
               fill=(0, 0, 0), font=font)
        img.save("../../files/img/example_%s.png" % i)


def create_images():
    # 创建 PNG 图像
    img = Image.new('RGB', (400, 300), color='white')
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('Arial Unicode.ttf', 36)
    d.text((100, 150), "PNG Example", fill=(0, 0, 0), font=font)
    img.save('../../files/example.png')

    # 创建 JPEG 图像
    img = Image.new('RGB', (800, 600), color='skyblue')
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('Arial Unicode.ttf', 24)
    d.text((200, 300), "JPEG Example", fill=(255, 255, 255), font=font)
    img.save('../../files/example.jpg')

    # 创建 GIF 图像
    img = Image.new('RGB', (200, 150), color='yellowgreen')
    d = ImageDraw.Draw(img)
    d.rectangle([(50, 50), (150, 100)], outline='black', fill='red')
    font = ImageFont.truetype('Arial Unicode.ttf', 18)
    d.text((10, 130), "GIF Example", fill=(0, 0, 0), font=font)
    img.save('../../files/example.gif')

    # 创建 BMP 图像
    img = Image.new('RGB', (500, 200), color='white')
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('Arial Unicode.ttf', 28)
    d.text((100, 100), "BMP Example", fill=(255, 255, 255), font=font)
    img.save('../../files/example.bmp')

    # 创建 TIFF 图像
    img = Image.new('RGB', (1200, 900), color='magenta')
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('Arial Unicode.ttf', 42)
    d.text((500, 450), "TIFF Example", fill=(255, 255, 0), font=font)
    img.save('../../files/example.tiff')


if __name__ == '__main__':
    create_images()
