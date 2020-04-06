from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Firefox(executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages"
                                           "\\geckodriver.exe")
# 让司机加载一个网页
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc")
time.sleep(10)
num = driver.window_handles
# 获取当前页句柄
driver.switch_to.window(num[0])
r = driver.find_element_by_xpath('//*[@id="76000D22440F_ICW_FZS"]')
print(r)
