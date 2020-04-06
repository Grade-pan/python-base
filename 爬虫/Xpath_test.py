import json
import os
import random

import pymysql
import requests


def test_06():
    url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=500' \
          '&page_start=0 '
    # 常用headers
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

    html = requests.get(url, headers={'User-Agent': headers[random.randint(1, 12)]})
    data = json.loads(html.text)
    news = data['subjects']
    Sum = 1
    cn = pymysql.connect(user='root', db='python', port=3306, password='123456', host='127.0.0.1')
    cursor = cn.cursor()
    cursor.execute('drop table if exists douban')
    cursor.execute('create table douban(id int  AUTO_INCREMENT PRIMARY KEY,name varchar(20),url varchar(50),'
                   'score varchar(20))')
    Sum = 1
    if os.path.exists('D:\\douban_tv.text'):
        os.remove('D:\\douban_tv.text')
    with open('D:\\douban_tv.text', 'a+') as f:
        f.write(' ' * 70 + '豆瓣热门电视剧' + '\n')
        print('文件创建成功')
        for i in news:
            cursor.execute('insert into douban (name,url,score) values (%s,%s,%s)', [i['title'], i['url'], i['rate']])
            f.write(str(Sum) + '  ' + i['title'] + '  ' + 'url:  ' + i['url'] + '  ' + '分数:  ' + i['rate'] + '\n')
            f.write('-' * 100 + '\n')
            f.flush()
            Sum = Sum + 1
        cn.commit()
    cn.close()
    f.close()
    print('数据写入文件成功')
    print('数据写入数据库成功')


if __name__ == '__main__':
    test_06()
