from selenium import webdriver
import time

# 1.访问百度
driver = webdriver.Firefox(executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages"
                                           "\\geckodriver.exe")
driver.get("http://www.baidu.com")

# 2.搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

# 3.休眠2s目的是获得服务器的响应内容，如果不使用休眠可能报错
time.sleep(2)

# 4.通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,450);"
driver.execute_script(js)
time.sleep(3)

driver.close()
