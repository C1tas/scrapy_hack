# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import logging

from scrapy.conf import settings
from scrapy.exceptions import DropItem



class HackPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    collection_name = 'house'
    def __init__(self, mongo_url, mongo_port, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url = settings['MONGODB_SERVER'],
            mongo_port = settings['MONGODB_PORT'],
            mongo_db = settings['MONGODB_DB']
        )

    def open_spider(self, spider):
        try:
            self.client = pymongo.MongoClient(
                self.mongo_url,
                self.mongo_port
            )
            self.db = self.client[self.mongo_db]
        except Exception as e:
            logging.log(logging.ERROR, "There is a error happend")

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item:
            # print(item)
            self.db[self.collection_name].insert(dict(item))
            # logging.log(logging.WARNING, "FUCKC!!!!THAT!!!!!!!!!!!!!!!!!!!!")
            # raise DropItem("Duplicate item found: %s" % item)
        else:
            # raise DropItem("Duplicate item found: %s" % item)
            logging.log(logging.WARNING, "FUCKC!!!!!!!!!!!!!!!!!!!!!!!!")
        return item

