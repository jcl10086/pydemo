#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

binary_location = '/opt/google/chrome/google-chrome'
chrome_driver_binary = '/opt/google/chromedriver/chromedriver'

chrome_options = Options()
chrome_options.binary_location = binary_location
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

chromedriver = chrome_driver_binary
os.environ["webdriver.chrome.driver"] = chromedriver

BROWSER = webdriver.Chrome(executable_path='/opt/google/chrome/google-chrome', chrome_options=chrome_options)

#WAIT = WebDriverWait(BROWSER, 5)
URL = "http://www.baidu.com"
BROWSER.get(URL)
BROWSER.save_screenshot('aa.png')