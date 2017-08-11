# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from meizi import settings

class MeiziPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        for image_url in item['images_url']:
            yield scrapy.Request(image_url)

    def item_completed(self,results,item,info):
        return item
