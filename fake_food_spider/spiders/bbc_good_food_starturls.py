# -*- coding: utf-8 -*-
import scrapy


class BbcGoodFoodStarturlsSpider(scrapy.Spider):
    name = 'bbc-good-food-starturls'
    allowed_domains = ['bbcgoodfood.com']
    start_urls = ['http://bbcgoodfood.com/']

    def parse(self, response):
        pass
