# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem


class HackPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    def __init__(self):
        self.mongo_url = settings['MONGODB_SERVER']
        self.mongo_port = settings['MONGODB_PORT']
        self.mongo_db = settings['MONGODB_DB']

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url = settings['MONGODB_SERVER'],
            mongo_port = settings['MONGODB_PORT'],
            mongo_db = settings['MONGODB_DB']
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        vaild = True
        print(item)
        for data in item:
            if not data:
                vaild = False
                raise DropItem("Missing {0}!".format(data))
            if vaild:
                self.collection.insert(dict(item))
                log.msg("House added to MongoDB database~",
                        level=log.DEBUG, spider=spider)
            return item
