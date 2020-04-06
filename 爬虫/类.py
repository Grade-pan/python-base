from pyquery import PyQuery as pq


class Foo:
    @classmethod
    def get_this(cls, url_):
        html = pq(url_)
        text = html('div').filter('.read-content')
        text = text('p')
        for i in text:
            print(i.text)

    @classmethod
    def get_next(cls, url_):
        html = pq(url_)
        html1 = html('div').filter('.read-page')
        html1 = html1('a').eq(-1).attr('href')
        return html1


if __name__ == '__main__':
    foo01 = Foo()
    url = foo01.get_next('http://book.zhulang.com/696901/19607.html')
    foo01.get_this(url)
    print(foo01.get_next(url))
