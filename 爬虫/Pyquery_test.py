import requests
from pyquery import PyQuery as pq
from requests import RequestException


class get_novel:
    def get_html(self, url_):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/69.0.3497.100 '
                          'Safari/537.36 '
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.text
            return None
        except RequestException:
            print('请求页面出错', url)
            return None

    def test_06(self, url_):
        html = pq(url_)
        text = html('div').filter('.read-content')
        text = text('p')
        for i in text:
            print(i.text)

    def test_07(self, url_):
        html = pq(url_)
        html1 = html('div').filter('.read-page')
        html1 = html1('a').eq(-1).attr('href')
        return html1


if __name__ == '__main__':
    x = get_novel()
    url = 'http://book.zhulang.com/696901/18530.html'
    url1 = x.get_html(url)
    x.test_06(url)
    for i in range(1, 10):
        url = url
        url = x.test_07(url)
        url1 = x.get_html(url)
        x.test_06(url1)
