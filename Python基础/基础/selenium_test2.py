from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox(executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages"
                                           "\\geckodriver.exe")
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 1.鼠标悬停至“设置”链接
driver.find_element_by_link_text('设置').click()
time.sleep(2)
# 2.打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)

# 3.搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('50')  # 显示50条
driver.find_element_by_link_text("保存设置").click()
time.sleep(3)
driver.quit()
