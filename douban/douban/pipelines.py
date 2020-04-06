# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

from pymongo import MongoClient

client = MongoClient()
collection = client['douban']['douban_movie']


class DoubanPipeline(object):
    def __init__(self):
        self.f = open('lujian.csv', 'w')
        self.writer = csv.writer(self.f)
        self.writer.writerow(['id', 'song', 'nickname', 'avatarurl', 'hotcomment_like', 'comments'])

    def process_item(self, item, spider):
        print(item)
