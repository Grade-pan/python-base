import random

import pymysql
import requests
from lxml import etree

# //div[@id="CommonListCell"]//div[@class="post-list"]//div[@class="post-header"]//a
headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 "
    "Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 "
    "Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 "
    "Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "]


def delete_sql():
    con = pymysql.connect(user='root', password='123456', port=3306, host='127.0.0.1', db='python')
    cursor = con.cursor()
    cursor.execute('drop table if exists fuli')


def get_shop(url_):
    con = pymysql.connect(user='root', password='123456', port=3306, host='127.0.0.1', db='python')
    cursor = con.cursor()
    if cursor.execute('show tables like "fuli"'):
        pass
    else:
        cursor.execute('create table fuli (id int  AUTO_INCREMENT PRIMARY KEY,huodong varchar(200),link varchar(1000),'
                       'time_p varchar(100))')
    html = requests.get(url_, headers={'User-Agent': headers[random.randint(1, 12)]})
    # encode????????????ISO-8859-1?????????unicode
    html = html.text.encode("ISO-8859-1")
    # decode??????,???unicode?????????utf-8
    html = html.decode("utf-8")
    html1 = etree.HTML(html)
    data = html1.xpath('//div[@id="CommonListCell"]//div[@class="post-list"]//div[@class="post-header"]//a')
    data1 = html1.xpath('//div[@id="CommonListCell"]//div[@class="post-list"]//div[@class="post-meta"]//span['
                        '@class="ptime"]//span')
    for i, j in zip(data, data1):
        # print(i.text + 'https://www.xhzyw.com' + i.get('href') + str(j.text))
        # print('-' * 60)
        cursor.execute('insert into fuli (huodong,link,time_p) values (%s,%s,%s)',
                       [i.text, 'https://www.xhzyw.com' + i.get('href'), str(j.text)])
    con.commit()

    con.close()


def get_url(url_):
    html = requests.get(url_, headers={'User_agent': headers[random.randint(1, 12)]})
    # encode????????????ISO-8859-1?????????unicode
    html = html.text.encode("ISO-8859-1")
    # decode??????,???unicode?????????utf-8
    html = html.decode("utf-8")
    html1 = etree.HTML(html)
    url_ = html1.xpath("//div[@id='content-list']//li//a")
    return 'https://www.xhzyw.com/huodong/' + url_[-2].get('href')


if __name__ == '__main__':
    delete_sql()
    url = 'https://www.xhzyw.com/huodong/'
    get_shop(url)
    for i in range(1, 10):
        url1 = url
        url = get_url(url1)
        get_shop(url)
    print('????????????')
