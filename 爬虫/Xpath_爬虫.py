import pymysql
import requests
from lxml import etree


def f():
    conn = pymysql.connect(user='root', password="123456", database='python', host='127.0.0.1', port=3306,
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute('drop table if exists IP1')
    cursor.execute('create table IP1 (id int AUTO_INCREMENT PRIMARY KEY, ip varchar(200),port varchar(200),'
                   'address varchar(200),Character_net varchar(200),Time_now varchar(200))')
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/67.0.3396.99 Safari/537.36",
    }
    Sum = 1
    for i in range(1, 21):
        url = 'http://www.89ip.cn/index_' + str(i) + '.html'
        response = requests.get(url, headers=header)
        html = etree.HTML(response.text)
        for i in range(1, 16):
            xpath_l = '/html/body/div[4]/div[1]/div/div[1]/table/tbody/tr' + str([i]) + '/td'
            html_data = html.xpath(xpath_l)
            A_list = list()
            for i in html_data:
                A_list.append(i.text)
            try:
                cursor.execute(
                    'insert into IP1 (ip,port,address,Character_net,Time_now) values (%s, %s,%s,%s,%s)',
                    [A_list[0], A_list[1], A_list[2], A_list[3], A_list[-1]])
                print('第%d条数据写入成功' % Sum)
                Sum = Sum + 1
                conn.commit()
            except:
                print('数据获取完毕')
    cursor.close()
    conn.close()


if __name__ == '__main__':
    f()
