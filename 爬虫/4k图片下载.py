import random
import re
import urllib.request

import pymysql
import requests
from bs4 import BeautifulSoup

import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 ' \
             'Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400 '
headers = {"User-Agent": user_agent}
print(headers)

def get_url(html_url):
    url = html_url
    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    for k in soup.find_all('div', class_='slist'):
        a = k.find_all('img')
        a1 = k.find_all('a')
        m = re.findall(r'[\'\"\s]+[^\"\']+\.jpg[\"\']?', str(a))  # 匹配src
        n = re.findall(r'<a.*? title="(.*?)".*?>.*?</a>', str(a1))  # 匹配title
        for i in n:
            with open('D:\\images\\图片名称.txt', 'a') as f:
                f.write(str(i) + '\n')
                f.flush()
        f.close()
        print('图片名称获取成功')
        for i in m:
            with open('D:\\images\\link.txt', 'a') as f:
                i = str(i).replace('"', 'm', 1)
                f.write('http://pic.netbian.co' + str(i).replace('"', ' ', 1) + '\n')
                f.flush()
        f.close()
    print('链接获取成功')


def get_picture():
    Sum = 0
    with open('D:\\images\\link.txt', 'r') as f:
        while True:
            A_url = f.readline()
            if not A_url:
                break
            request = urllib.request.Request(A_url, headers=headers)
            try:
                response = urllib.request.urlopen(request)
                img_name = 'images' + str(Sum) + '.png'
                filename = "D:\\images\\" + img_name
                if response.getcode() == 200:
                    with open(filename, "wb") as f2:
                        f2.write(response.read())  # 将内容写入图片
                        time.sleep(random.random() * 3)
            except:
                return "下载失败"
            Sum = Sum + 1
            print('第%d张图片下载成功' % Sum)
    f.close()


def get_Mysql():
    Sum = 0
    A_text = list()
    with open('D:\\images\\图片名称.txt', 'r') as f1:
        while True:
            B_str = f1.readline()
            if not B_str:
                break
            B_str = str(B_str)
            A_text.append(B_str)
    conn = pymysql.connect(user='root', password='123456', host='127.0.0.1', port=3306, database='python')
    cursor = conn.cursor()
    cursor.execute('drop table if exists picture')
    cursor.execute('create table picture (id int  AUTO_INCREMENT PRIMARY KEY,  name varchar(2000),link varchar(2000))')
    with open('D:\\images\\link.txt', 'r') as f:
        while True:
            A_str = f.readline()
            if not A_str:
                break
            cursor.execute(
                'insert into picture (name, link) values (%s, %s)', [A_text[Sum], str(A_str)])
            conn.commit()
            Sum = Sum + 1
        cursor.close()
        conn.close()
        print('数据写入数据库成功')
    f.close()


if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'  # 代理网站
    img_url = "http://pic.netbian.com/"  # 爬取网站
    get_url(img_url)
    get_picture()
    get_Mysql()
