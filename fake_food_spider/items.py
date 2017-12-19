# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FakeFoodStartURL(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    url_hash = scrapy.Field()
    is_recipe = scrapy.Field()
    name = scrapy.Field()
    s_id = scrapy.Field()

class FakeFoodRecipe(scrapy.Item):
    url = scrapy.Field()
    url_hash = scrapy.Field()
    name = scrapy.Field()
    date_published = scrapy.Field()
    ingredients = scrapy.Field()
    method = scrapy.Field()
