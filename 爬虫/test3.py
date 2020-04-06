import requests
from lxml import etree

def get_url_true():
    url='http://www.weather.com.cn/weather/101180101.shtml'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                                 'like Gecko) Chrome/78.0.3904.70 Safari/537.36'})
    # encode解码，将ISO-8859-1解码成unicode
    html = r.text.encode("ISO-8859-1")
    # decode编码,将unicode编码成utf-8
    html = html.decode("utf-8")
    html1 = etree.HTML(html)
    list_weather = []
    data_time = html1.xpath('//div[@class="left fl"]//ul//li//h1')
    data_high_temperature = html1.xpath('//div[@class="left fl"]//ul//li//p[@class="tem"]//span')
    data_low_temperature = html1.xpath('//div[@class="left fl"]//ul//p[@class="tem"]//i')
    data_wind = html1.xpath('//div[@class="left fl"]//ul//li//p[@class="win"]//em//span')  # 获取title标签
    data_wind_level = html1.xpath('//div[@class="left fl"]//ul//li//p[@class="win"]//i')
    data_weather = html1.xpath('//div[@class="left fl"]//ul//li//p[@class="wea"]')  # 获取title标签
    for i in range(0, len(data_weather)):
        Item = {'时间': data_time[i].text,
                '天气': data_weather[i].get('title'),
                '高温': data_high_temperature[i - 1].text,
                '低温': data_low_temperature[i].text,
                '风向': data_wind[i].get('title'),
                '风力': data_wind_level[i].text
                }
        list_weather.append(Item)
    for i in list_weather:
        print(i)


if __name__ == "__main__":
    get_url_true()
