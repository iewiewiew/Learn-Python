# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/8 11:59
@description  playwright 例子
"""

import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

# 同步
with sync_playwright() as p:
    # 创建浏览器对象
    # browser = p.chromium.launch()
    # 默认情况下，Playwright 以无头模式运行浏览器。要查看浏览器 UI（有头模式），请在启动浏览器时传递 headless=False 标志，还可以使用 slow_mo 来减慢执行速度。
    # browser = p.chromium.launch(headless=False, slow_mo=500)
    # 打开开发者模式
    browser = p.chromium.launch(devtools=True)
    page = browser.new_page()
    page.goto("https://www.baidu.com/")
    page.screenshot(path="example.png")
    print(page.title())
    # 等待5秒
    page.wait_for_timeout(5000)
    browser.close()


# 异步
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.baidu.com/")
        print(await page.title())
        await browser.close()


asyncio.run(main())
