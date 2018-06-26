# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    vertical_src = scrapy.Field()
    nickname= scrapy.Field()
    anchor_city= scrapy.Field()
    room_url= scrapy.Field()
    room_name= scrapy.Field()
    image_path = scrapy.Field()