# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity


def remove_text(x):

    return x.strip('\n ')


class FoodNetworkLoader(ItemLoader):

    default_output_processor = TakeFirst()

    ingredients_in = Identity()
    ingredients_out = Join(separator=u'\n')

    method_in = MapCompose(remove_text)
    method_out = Join(separator=u'\n')
