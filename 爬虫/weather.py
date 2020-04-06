import csv
import random

import requests
from lxml import etree

# 城市列表如下：
# http://hebei.weather.com.cn/m2/j/hebei/public/city.min.js
# 目前支持北京、天津、重庆三个城市7天天气预报
# 支持河南天气更新
# 18点后获取天气预报将get_text()方法中的0改为1
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


def get_province():
    url = 'http://www.weather.com.cn/province/'
    r = requests.get(url, headers={'User-Agent': headers[random.randint(1, 11)]})
    # encode解码，将ISO-8859-1解码成unicode
    html = r.text.encode("ISO-8859-1")
    # decode编码,将unicode编码成utf-8
    html = html.decode("utf-8")
    html1 = etree.HTML(html)
    data = html1.xpath('/html/body/div[2]/div[2]/ul/li/a')
    list_province = []
    for i in data:
        item = {'省辖市': i.text, '链接': i.get('href')}
        list_province.append(item)
    return list_province


def get_city_link(ul, ulink, list_weather):
    ul = ul
    ulink = ulink
    if ul in list_weather:
        url = ulink
        r = requests.get(url, headers={'User-Agent': headers[random.randint(1, 11)]})
        # encode解码，将ISO-8859-1解码成unicode
        html = r.text.encode("ISO-8859-1")
        # decode编码,将unicode编码成utf-8
        html = html.decode("utf-8")
        html1 = etree.HTML(html)
        return html1
    else:
        pass


def get_special(ulink):
    url = ulink
    r = requests.get(url, headers={'User-Agent': headers[random.randint(1, 11)]})
    # encode解码，将ISO-8859-1解码成unicode
    html = r.text.encode("ISO-8859-1")
    # decode编码,将unicode编码成utf-8
    html = html.decode("utf-8")
    html1 = etree.HTML(html)
    return html1


def get_city(list_):
    # 上海天气10月23日网页改版
    list_all = ['北京', '天津', '重庆']
    list_null = ['山西', '湖北', '青海']
    # 安徽  http://www.weather.com.cn/anhui/index.shtml
    # 完整url
    # /html/body/div[1]/div[3]/div/span/a[1]
    # 广东
    # /html/body/div[2]/ul/li[6]/a
    # 广西
    # /html/body/div[1]/div[1]/div[2]/div/span/a[4]
    # 黑龙江
    # /html/body/div[3]/div/a[4]
    list_special_city = ['台湾', '香港', '澳门', '河北']
    list_http = ['河南', '山东', '陕西', '江苏', '湖南', '福建', '海南', '云南', '四川', '西藏', '江西', '新疆', '甘肃', '宁夏', '内蒙古', '吉林',
                 '辽宁']
    list_city = []
    for i in list_:
        ul = i['省辖市']
        ulink = i['链接']
        if ul in list_all:
            html = get_city_link(ul, ulink, list_all)
            data = html.xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/span[1]/a')
            for i in data:
                item = {'市,区': i.text, '链接': i.get('href')}
                list_city.append(item)
        if ul in list_http:
            html1 = get_city_link(ul, ulink, list_http)
            data1 = html1.xpath('/html/body/div[1]/div[2]/div/span/a')
            for i in data1:
                item = {'市,区': i.text, '链接': (ulink + i.get('href'))}
                list_city.append(item)
        if ul in list_null:
            html2 = get_city_link(ul, ulink, list_null)
            data2 = html2.xpath('/html/body/div[2]/div[2]/div/span/a')
            for i in data2:
                item = {'市,区': i.text, '链接': (ulink + i.get('href'))}
                list_city.append(item)
        if ul in list_special_city:
            pass
        if ul == '安徽':
            html = get_special(' http://www.weather.com.cn/anhui/index.shtml')
            data = html.xpath('/html/body/div[1]/div[3]/div/span/a')
            for i in data:
                item = {'市,区': i.text, '链接': i.get('href')}
                list_city.append(item)
        if ul == '广东':
            html = get_special(ulink)
            data = html.xpath(' /html/body/div[2]/ul/li[6]/a')
            for i in data:
                item = {'市,区': i.text, '链接': (ulink + i.get('href'))}
                list_city.append(item)
        if ul == '广西':
            html = get_special(ulink)
            data = html.xpath('/html/body/div[1]/div[1]/div[2]/div/span/a')
            for i in data:
                item = {'市,区': i.text, '链接': (ulink + i.get('href'))}
                list_city.append(item)
        if ul == '黑龙江':
            html = get_special(ulink)
            data = html.xpath('/html/body/div[3]/div/a')
            for i in data:
                item = {'市,区': i.text, '链接': (ulink + i.get('href'))}
                list_city.append(item)
    return list_city


# 北京、天津、重庆
def get_weather():
    # 风向仅供参考
    All_url = get_city(get_province())
    list_weather = []
    for i in All_url:
        url = i['链接']
        name = i['市,区']
        r = requests.get(url, headers={'User-Agent': headers[random.randint(1, 11)]})
        # encode解码，将ISO-8859-1解码成unicode
        html = r.text.encode("ISO-8859-1")
        # decode编码,将unicode编码成utf-8
        html = html.decode("utf-8")
        html1 = etree.HTML(html)
        data_time = html1.xpath('//div[@class="con today clearfix"]//ul[@class="t clearfix"]//li//h1')
        data_weather = html1.xpath('//div[@class="con today clearfix"]//ul[@class="t clearfix"]//li//p[@class="wea"]')
        data_temperature = html1.xpath(
            '//div[@class="con today clearfix"]//ul[@class="t clearfix"]//li//p[@class="tem"]//i')
        data_wind_level = html1.xpath(
            '//div[@class="con today clearfix"]//ul[@class="t clearfix"]//li//p[@class="win"]//i')
        data_wind = html1.xpath(
            '//div[@class="con today clearfix"]//ul[@class="t clearfix"]//li//p[@class="win"]//em//span')
        for i in range(0, len(data_time)):
            Item = {'城市': name,
                    '时间': data_time[i].text,
                    '天气': data_weather[i].text,
                    '温度': data_temperature[i].text,
                    '风力': data_wind_level[i].text,
                    '风向': data_wind[i].get('title')}
            list_weather.append(Item)
    csv_File = open("D:\\beijing_tianjin_chongqing_weather.csv", 'w', newline='')
    try:
        writer = csv.writer(csv_File)
        writer.writerow(('城市', '时间', '天气', '实时温度', '风力', '风向'))
        for i in list_weather:
            writer.writerow((i['城市'], i['时间'], i['天气'], i['温度'], i['风力'], i['风向']))
    finally:
        csv_File.close()
    print('北京，重庆，天津天气获取成功')


def get_henan():
    All_url = get_city(get_province())
    list_henan = ['郑州', '安阳', '濮阳', '鹤壁', '焦作', '济源', '新乡', '三门峡', '洛阳', '平顶山', '许昌', '漯河', '开封', '周口', '商丘', '南阳',
                  '信阳', '驻马店']
    list_weather1 = []
    for i in All_url:
        url = i['链接']
        name = i['市,区']
        if name in list_henan:
            url = url
            r = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                              'like Gecko) Chrome/78.0.3904.70 Safari/537.36'})
            # encode解码，将ISO-8859-1解码成unicode
            html = r.text.encode("ISO-8859-1")
            # decode编码,将unicode编码成utf-8
            html = html.decode("utf-8")
            html1 = etree.HTML(html)
            url_true = html1.xpath('//div[@class="gsbox"]//div[@class="forecastBox"]//dl//dt//a[1]')
            Item = {
                '城市': name,
                '链接': url_true[0].get('href')
            }
            list_weather1.append(Item)
    return list_weather1


def get_text():
    list_weather1 = []
    list_weather = get_henan()
    for i in list_weather:
        url = i['链接']
        name = i['城市']
        r = requests.get(url,
                         headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                                'like Gecko) Chrome/78.0.3904.70 Safari/537.36'})
        # encode解码，将ISO-8859-1解码成unicode
        html = r.text.encode("ISO-8859-1")
        # decode编码,将unicode编码成utf-8
        html = html.decode("utf-8")
        html1 = etree.HTML(html)
        data_time = html1.xpath('//div[@class="left fl"]//ul//li//h1')
        data_high_temperature = html1.xpath('//div[@class="left fl"]//ul//li//p[@class="tem"]//span')
        data_low_temperature = html1.xpath('//div[@class="left fl"]//ul//p[@class="tem"]//i')
        data_wind = html1.xpath('//div[@class="left fl"]//ul//li//p[@class="win"]//em//span')  # 获取title标签
        data_wind_level = html1.xpath('//div[@class="left fl"]//ul//li//p[@class="win"]//i')
        data_weather = html1.xpath('//div[@class="left fl"]//ul//li//p[@class="wea"]')  # 获取title标签
        for i in range(0, len(data_time)):
            Item = {'城市': name,
                    '时间': data_time[i].text,
                    '天气': data_weather[i].get('title'),
                    '高温': data_high_temperature[i - 1].text,
                    '低温': data_low_temperature[i].text,
                    '风向': data_wind[i].get('title'),
                    '风力': data_wind_level[i].text
                    }
            list_weather1.append(Item)
    csv_File = open("D:\\henan_weather.csv", 'w', newline='')
    try:
        writer = csv.writer(csv_File)
        writer.writerow(('城市', '时间', '天气', '高温', '低温', '风力', '风向'))
        for i in list_weather1:
            writer.writerow((i['城市'], i['时间'], i['天气'], i['高温'], i['低温'], i['风力'], i['风向']))
    finally:
        csv_File.close()
    print('河南天气获取成功')


if __name__ == '__main__':
    get_text()
    get_weather()
