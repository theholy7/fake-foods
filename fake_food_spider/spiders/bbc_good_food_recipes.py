# -*- coding: utf-8 -*-
import scrapy
from ..database import StartUrl



class BbcGoodFoodRecipesSpider(scrapy.Spider):
    name = 'bbc_good_food_recipes'
    allowed_domains = ['bbcgoodfood.com']
    start_urls = ['http://bbcgoodfood.com/']

    def start_requests(self):
        bbc_start_urls = (db.query(StartUrl)
                            .first())
        


    def parse(self, response):
        pass
