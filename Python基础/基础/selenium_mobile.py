from selenium import webdriver

import time

driver = webdriver.Firefox(executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages"
                                           "\\geckodriver.exe")
driver.get('http://www.weather.com.cn/')
time.sleep(5)
list_ = ['郑州', '洛阳', '新乡', '鹤壁', '安阳', '济源', '三门峡', '平顶山', '南阳', '漯河', '驻马店', '信阳', '许昌', '周口', '商丘', '焦作', '开封', '濮阳']
for i in range(0, len(list_)):
    driver.find_element_by_id('txtZip').send_keys(list_[i])
    driver.find_element_by_id('btnZip').click()
    time.sleep(5)
    num = driver.window_handles
    # 获取当前页句柄
    driver.switch_to.window(num[i+1])
    # 跳转到新标签页
    text = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[2]/input[1]').get_attribute('value')
    print(list_[i], text)
driver.quit()
