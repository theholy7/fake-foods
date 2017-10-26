# -*- coding: utf-8 -*-
import scrapy
import re


class BbcGoodFoodStarturlsSpider(scrapy.Spider):
    name = 'bbc-good-food-starturls'
    allowed_domains = ['bbcgoodfood.com']
    start_urls = ['http://bbcgoodfood.com/']

    def parse(self, response):
        # collect all /recipes/ urls and make new request
        # check if they have the recipe title class
        # save url as recipe if recipe title class is in html
        # then save an is_recipe = True in the item
