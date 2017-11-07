# -*- coding: utf-8 -*-
import scrapy


class BbcGoodFoodRecipesSpider(scrapy.Spider):
    name = 'bbc_good_food_recipes'
    allowed_domains = ['bbcgoodfood.com']
    start_urls = ['http://bbcgoodfood.com/']

    def parse(self, response):
        pass
