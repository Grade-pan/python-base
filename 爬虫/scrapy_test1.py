from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class JobboleSpider(object):
    pass


def __init__(self):
    self.browser = webdriver.Chrome(
        executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages"
                        "\\geckodriver.exe")
    super(JobboleSpider, self).__init__()
    # 信号的作用：当spider关闭的时候我们做什么事情
    dispatcher.connect(self.spider_closed, signals.spider_closed)


def spider_closed(self, spider):
    # 当爬虫退出的时候关闭Chrome
    print("spider closed")
    self.browser.quit()
