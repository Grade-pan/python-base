from selenium import webdriver

import time

browser = webdriver.Firefox(executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages"
                                            "\\geckodriver.exe")
browser.get("http://www.youdao.com")

# 1.打印cookie信息
print('=====================================')
print("打印cookie信息为：")
print(browser.get_cookies)

# 2.添加cookie信息
dict = {'name': "name", 'value': 'Kaina'}
browser.add_cookie(dict)

print('=====================================')
print('添加cookie信息为：')
# 3.遍历打印cookie信息
for cookie in browser.get_cookies():
    print('%s----%s\n' % (cookie['name'], cookie['value']))

# 4.删除一个cookie
browser.delete_cookie('name')
print('=====================================')
print('删除一个cookie')
for cookie in browser.get_cookies():
    print('%s----%s\n' % (cookie['name'], cookie['value']))

print('=====================================')
print('删除所有cookie后：')
# 5.删除所有cookie,无需传递参数
browser.delete_all_cookies()
for cookie in browser.get_cookies():
    print('%s----%s\n' % (cookie['name'], cookie['value']))

time.sleep(3)
browser.close()
