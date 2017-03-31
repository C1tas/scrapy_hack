
from scrapy_redis.spiders import RedisSpider

import json



class Beijingalive(RedisSpider):
    name = "bj_alive"
    start_urls = [
        'https://api.douban.com/v2/group/beijingzufang/'
    ]

    def parse(self, response):
        print(response.body)
        pass
