from bs4 import BeautifulSoup
import requests
import pandas as pd

url = ['http://www.weather.com.cn/textFC/hb.shtml', 'http://www.weather.com.cn/textFC/db.shtml',
       'http://www.weather.com.cn/textFC/hd.shtml',
       'http://www.weather.com.cn/textFC/hz.shtml', 'http://www.weather.com.cn/textFC/hn.shtml',
       'http://www.weather.com.cn/textFC/xb.shtml',
       'http://www.weather.com.cn/textFC/xn.shtml', 'http://www.weather.com.cn/textFC/gat.shtml']
place = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']  # 华北，东北，华东，华中，华南，西北，西南，港澳台
for i in range(0, len(place)):
    res = requests.get(url[i])
    html = res.text.encode("ISO-8859-1")
    # decode编码,将unicode编码成utf-8
    html = html.decode("utf-8")
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.select('table')
    df_list = []
    for table in tables:
        df_list.append(pd.concat(pd.read_html(table.prettify())))
    df = pd.concat(df_list)
    df.to_excel('D:\\China_weather\\' + str(place[i]) + '_weather.xlsx')
    print(place[i], '输出成功')
