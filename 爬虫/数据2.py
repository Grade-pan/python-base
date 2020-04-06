import re

import requests
from bs4 import BeautifulSoup

Sum = 2
while Sum <= 100:
    with open('E:\\aaa.text', 'r') as f:
        url_ = f.readline()
        print(url_)
        f.close
    url = url_
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 " \
                 "Safari/537.36 "
    headers = {"User-Agent": user_agent}
    f = requests.get(url, headers=headers)  # Get该网页从而获取该html内容
    soup = BeautifulSoup(f.content, 'lxml')  # 用lxml解析器解析该网页的内容, 好像f.text也是返回的html
    # print(f.content.decode())								#尝试打印出网页内容,看是否获取成功
    # content = soup.find_all('div', class_="p12")  # 尝试获取节点，因为calss和关键字冲突，所以改名class_
    for k in soup.find_all('div', class_='read-content j_readContent'):
        a = k.find_all('p')
        Str_A = str(a).replace('<p>', '  ')
        Str_B = Str_A.replace('</p>', '\n')
        Str_C = Str_B.replace(',', '')
        Str_D = Str_C.replace('[', '')
        Str_E = Str_D.replace(']', '')
    with open('E:\\aa.text', 'a') as f:
        f.write('章节' + "\n")
        f.write(Str_E)
        f.flush()
        f.close()
    for k in soup.find_all('div', class_='chapter-control dib-wrap'):
        a = k.find_all('a', id='j_chapterNext')
        url1 = re.findall(r'<a\b[^>]+\bhref="([^"]*)"[^>]*>([\s\S]*?)</a>', str(a))  # 正则表达式匹配href
        with open('E:\\aaaa.text', 'a') as f:
            Sum1 = str(Sum)
            f.write('第' + Sum1 + '章节链接：     https:')
            f.write(url1[0][0] + '\n')
            f.flush()
            f.close()
        with open('E:\\aaa.text', 'w') as f:
            f.write('https:' + url1[0][0])
            f.flush()
            f.close()
    Sum = Sum + 1
print('爬取完成')
