from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages"
                                           "\\geckodriver.exe")
driver.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')

# driver.find_element_by_id('txtZip').send_keys('郑州')
# driver.find_element_by_id('btnZip').click()
# time.sleep(2)
time.sleep(20)
# 1.截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("D:\\baidu_img.png")
print('截图成功')
driver.quit()
