# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem

class DouyuImgSpider(scrapy.Spider):
    name = 'douyu_img'
    allowed_domains = ['douyu.com']
    global base_url
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset={}'

    start_urls = [base_url.format(i) for i in range(0,501,100)]


    def parse(self, response):

        node_list=json.loads(response.body.decode())["data"]
        for node in node_list:
            item = DouyuItem()
            item["vertical_src"] =node["vertical_src"]
            item["nickname"] = node["nickname"]
            item["anchor_city"] = node["anchor_city"]
            item["room_url"] = "https://www.douyu.com/" +node["room_id"]
            item["room_name"] = node["room_name"]


            yield item