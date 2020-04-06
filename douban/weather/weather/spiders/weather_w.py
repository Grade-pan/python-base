# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

import time


class WeatherWSpider(scrapy.Spider):
    name = 'weather_w'
    allowed_domains = ['www.weather.com.cn']
    start_urls = ['http://www.weather.com.cn/']

    def get_url(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages"
                                                   "\\geckodriver.exe")
        driver.get('http://www.weather.com.cn/')
        time.sleep(5)
        driver.find_element_by_id('txtZip').send_keys('郑州')
        driver.find_element_by_id('btnZip').click()
        time.sleep(5)

    def parse(self, response):
        pass
