import scrapy
import json

from hack.items import HackItem

class Hack_Douban(scrapy.Spider):
    name = "hack_douban"

    start_urls = [
        'https://api.douban.com/v2/group/beijingzufang/topics',
    ]

    def parse(self, response):
        print(response.body)
        tmp_json = json.loads(response.body.decode('UTF-8'))
        item = HackItem()
        item['count'] = tmp_json['count']
        print (tmp_json['count'])
        yield item
