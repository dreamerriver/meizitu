# -*- coding: utf-8 -*-
import scrapy
from meizi.items import MeiziItem 
import json


class MeituSpider(scrapy.Spider):
    name = 'meitu'
    allowed_domains=['image.baidu.com']
    start_urls=[
    'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=美女&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=美女&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn=%d' %i for i in range(0,30001,30)
    ]
    def parse(self, response):
        imgs = json.loads(response.body)['data']
        for img in imgs:
            item = MeiziItem()
            try:
                item['images_url']=[img['middleURL']]
                yield item
            except Exception as e:
                print(e)
