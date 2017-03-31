
# -*- coding: utf-8 -*-
import scrapy
import re

class ToGetComments(scrapy.Spider):
    name = "get_comments"
    start_urls = [
        'http://www.mocky.io/v2/58d8aa2a0f00008a1bdcc729',
    ]

    def parse(self, response):
        reg = re.compile(r'<!--([^>^-]*)-->')
        reg2 = re.compile(r'')
        reg.findall(str(response.body))
        print(reg)
        
