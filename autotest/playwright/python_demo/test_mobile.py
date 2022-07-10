# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/17 13:55
@description  移动端
"""

from playwright.sync_api import Playwright, sync_playwright
from time import sleep

##
with sync_playwright() as playwright:
    iphone_11 = playwright.devices['iPhone 11 Pro']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_11,
        locale='en-US',
        geolocation={'longitude': 12.492507, 'latitude': 41.889938},
        permissions=['geolocation']
    )
    page = context.new_page()
    page.goto('https://www.baidu.com')
    sleep(5)
    page.screenshot(path='colosseum-iphone.png')
    browser.close()
