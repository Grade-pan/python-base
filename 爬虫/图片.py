import requests
from bs4 import BeautifulSoup

# 设置初始url
url = 'https://www.58pic.com/newpic/35397692.html'

html = requests.get(url)
html = html.content
soup = BeautifulSoup(html, 'lxml')
soup.find_all('div', class_='pic-box')
# 获取图片链接和名称
for obj in soup.find_all('div', class_='pic-box'):
    link = obj.find_all('img')
    print(link)
for i in link:
    print(i)
print('爬取成功')
