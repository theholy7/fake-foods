# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..database import StartUrl
from ..connection import db



class BbcGoodFoodRecipesSpider(scrapy.Spider):
    name = 'bbc-good-food-recipes'
    allowed_domains = ['bbcgoodfood.com']
    start_urls = ['http://bbcgoodfood.com/']

    def start_requests(self):
        # overwride start_requests to get urls from db

        bbc_start_urls = (db.query(StartUrl)
                            .limit(5))

        rqs = [ Request(url=start_url.url, callback=self.parse)
                for start_url in bbc_start_urls]

        return rqs


    def parse(self, response):
        pass
