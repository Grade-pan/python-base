import pymysql
import requests
from lxml import etree
from bs4 import BeautifulSoup


# 代理IP的信息存储
def write_proxy(proxies):
    print(proxies)
    for proxy in proxies:
        with open("D:\\ip_proxy.txt", 'a+') as f:
            print("正在写入：", proxy)
            f.write(proxy + '\n')
    print("录入完成！！！")
    conn = pymysql.connect(user='root', password='123456', host='127.0.0.1', port=3306, database='python')
    cursor = conn.cursor()
    cursor.execute('drop table if exists IP')
    cursor.execute('create table IP (id int  AUTO_INCREMENT PRIMARY KEY, IP varchar(2000))')
    with open("D:\\ip_proxy.txt", 'r') as f:
        while True:
            A_ip = f.readline()
            if not A_ip:
                break
            cursor.execute(
                'insert into IP (IP) values (%s)', [str(A_ip)])
            conn.commit()
        cursor.close()
        conn.close()
    print('IP写入数据库成功')

# 解析网页，并得到网页中的代理IP
def get_proxy(html):
    # 对获取的页面进行解析
    selector = etree.HTML(html)
    print(selector)
    # print(selector.xpath("//title/text()"))
    proxies = []
    # 信息提取
    for each in selector.xpath("//tr[@class='odd'] | //tr[@class='']"):
        # ip.append(each[0])
        # 获取IP地址
        ip = each.xpath("./td[2]/text()")[0]
        # 获取端口
        port = each.xpath("./td[3]/text()")[0]
        # 拼接IP地址，端口号
        proxy = ip + ":" + port
        # 拼接的IP地址放入到定义的空列表中
        proxies.append(proxy)
    # 计算每个页面一共有几个IP地址
    print(len(proxies))
    test_proxies(proxies)


# 验证已得到IP的可用性，本段代码通过访问百度网址，返回的response状态码判断（是否可用）。
def test_proxies(proxies):
    proxies = proxies
    url = "http://www.baidu.com/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/67.0.3396.99 Safari/537.36",
    }
    normal_proxies = []
    count = 1
    for proxy in proxies:
        print("第%s个。。" % count)
        count += 1
        try:
            response = requests.get(url, headers=header, proxies={"http": proxy}, timeout=1)
            if response.status_code == 200:
                print("该代理IP可用：", proxy)
                normal_proxies.append(proxy)
            else:
                print("该代理IP不可用：", proxy)
        except Exception:
            print("该代理IP无效：", proxy)
            pass
    # print(normal_proxies)
    write_proxy(normal_proxies)


def get_html(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/67.0.3396.99 Safari/537.36",
    }
    response = requests.get(url, headers=header)
    # print(response.text)
    get_proxy(response.text)


if __name__ == "__main__":
    # 循环获取网址
    base_url = "http://www.89ip.cn/index_"
    for i in range(1, 4):
        url = base_url+str(i)+'.html'
        get_html(url)
