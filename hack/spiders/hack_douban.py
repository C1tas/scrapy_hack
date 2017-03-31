import scrapy
import json

class Hack_Douban(scrapy.Spider):
    name = "hack_douban"

    start_urls = [
        'https://api.douban.com/v2/group/beijingzufang/topics',
    ]

    def parse(self, response):
        tmp_json = json.loads(response.body.decode('UTF-8'))
        print (tmp_json['count'])
