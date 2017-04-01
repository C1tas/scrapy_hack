import scrapy
import json

from scrapy.exceptions import CloseSpider
from hack.items import HackItem

class Num_Generator:
    def __init__(self, start, end, step):
        self.i = start
        self.n = end
        self.step = step
        pass

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += self.step
            return i
        else:
            raise StopIteration


class Hack_Douban(scrapy.Spider):
    name = "hack_douban"

    start_urls = [
        'https://api.douban.com/v2/group/beijingzufang/',
    ]

    url = "https://api.douban.com/v2/group/beijingzufang/topics?count=%d&start=%d"
    a = Num_Generator(0, 25000, 100)
    def parse(self, response):
        try:
            x = self.a.next()
        except StopIteration:
            raise CloseSpider('finished')
        url = self.url % (100, x)
        yield scrapy.Request(url, self.parse)

        tmp_json = json.loads(response.body.decode('UTF-8'))
        for i in range(0, 100, 1):
            item = HackItem()
            tmp = tmp_json['topics'][i]
            item['alt'] = tmp['alt']
            item['author'] = tmp['author']
            item['comments_count'] = tmp['comments_count']
            item['content'] = tmp['content']
            item['created'] = tmp['created']
            item['id'] = tmp['id']
            item['like_count'] = tmp['like_count']
            item['locked'] = tmp['locked']
            item['photos'] = tmp['photos']
            item['share_url'] = tmp['share_url']
            item['title'] = tmp['title']
            item['updated'] = tmp['updated']
            yield item
