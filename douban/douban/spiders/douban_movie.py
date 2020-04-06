# -*- coding: utf-8 -*-
import json

import scrapy


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['douban.com/']
    start_urls = ['http://www.cbooo.cn/BoxOffice/getInland?pIndex=1&t=0']
    item = {}

    def parse(self, response):
        # 调用body_as_unicode()是为了能处理unicode编码的数据
        names = json.loads(response.body_as_unicode())
        Sum = 1
        item = self.item
        for i in names:
            item['电影'] = i['MovieName']
            item['票房'] = i['BoxOffice']
            item['地区'] = i['Area']
            item['类型'] = i['Genre_Main']
            item['上映时间'] = i['ReleaseTime']
            item['平均票价'] = i['AvgPrice']
            item['观影人数'] = i['AvgPeople']
            item['场均人次'] = i['defaultImage']
            # {
            #     # '排名': Sum,
            #     '电影': i['MovieName'],
            #     '票房': i['BoxOffice'],
            #     '地区': i['Area'],
            #     '类型': i['Genre_Main'],
            #     '上映时间': i['ReleaseTime'],
            #     '平均票价': i['AvgPrice'],
            #     '观影人数': i['AudienceCount'],
            #     '场均人次': i['AvgPeople'],
            #     # '封面地址': i['defaultImage']
            # # }
            Sum = Sum + 1
            yield item

    def start_requests(self):
        for i in range(1, 6):
            next_url = 'http://www.cbooo.cn/BoxOffice/getInland?pIndex=' + str(i) + '&t=0'
            yield scrapy.Request(next_url, callback=self.parse)

    # def parse_detail(self, response):
    #     # 获取之前传入的item
    #     item = response.meta["item"]
    #     yield item
