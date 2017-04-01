# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HackItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    alt = scrapy.Field()
    author = scrapy.Field()
    comments_count = scrapy.Field()
    content = scrapy.Field()
    created = scrapy.Field()
    id = scrapy.Field()
    like_count = scrapy.Field()
    locked = scrapy.Field()
    photos = scrapy.Field()
    share_url = scrapy.Field()
    title = scrapy.Field()
    updated = scrapy.Field()
