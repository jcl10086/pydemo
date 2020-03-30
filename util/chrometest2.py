#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)
try:
    picture_url=driver.save_screenshot('.\\baidu1.png')
    print("%s ：截图成功！！！" % picture_url)
except BaseException as msg:
    print("%s ：截图失败！！！" % msg)
driver.quit()