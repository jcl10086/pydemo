#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument('--no-sandbox')
# opt.add_argument('--disable-dev-shm-usage')
#opt.add_argument('--headless')
# opt.add_argument('blink-settings=imagesEnabled=false')
# opt.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options = opt, executable_path = 'D:/chromedriver_win32/chromedriver.exe')
# driver.set_page_load_timeout(100)
driver.get("http://10.10.204.83:31088/IncluldePage.html?pageid=10339&token=Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJkYXYtYWRtaW4iLCJjcmVhdGVkIjoxNTc3NjkwNDI0MjgzLCJleHAiOjE1Nzc3NzY4MjR9.p8lGnjwf2Kl-NezFpRBrHAbT1C6Iizdk6lY9iXMGMjXp3bP8V9umStdCx__ZpwlQTGOaMSicZYDmFNPpGLGhcQ&adjust=noAuto#/screen/default")
# driver.maximize_window()
time.sleep(30)

#接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
# width = driver.execute_script("return document.documentElement.scrollWidth")
# height = driver.execute_script("return document.documentElement.scrollHeight")
# print(width,height)
# #将浏览器的宽高设置成刚刚获取的宽高
# driver.set_window_size(2000, 3000)
# time.sleep(5)
#截图并关掉浏览器
driver.save_screenshot('test.png')
# driver.close()

# try:
#     picture_url=driver.save_screenshot('.\\baidu1.png')
#     print("%s ：截图成功！！！" % picture_url)
# except BaseException as msg:
#     print("%s ：截图失败！！！" % msg)
driver.quit()