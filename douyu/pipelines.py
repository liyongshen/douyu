# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from douyu.settings import IMAGES_STORE
import logging
from pymongo import MongoClient

class DouyuPipeline(ImagesPipeline):
    # 下载图片
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["vertical_src"])
    # 修改图片名字
    def item_completed(self, results, item, info):
        source_path = IMAGES_STORE + [x["path"] for ok,x in results if ok][0]
        item["image_path"] = IMAGES_STORE + "full/" +item["nickname"] +".jpg"
        try:
            os.rename(source_path,item["image_path"])
        except Exception as e:
            logging.error(e)
        return item


class MongoPipeline(object):

    def open_spider(self,spider):
        self.client = MongoClient()
        self.collection = self.client["douyu"]["yanzhi"]

    def process_item(self,item,spider):
        self.collection.insert(dict(item))

        return item

    def close_spider(self,spider):

        self.client.close()


