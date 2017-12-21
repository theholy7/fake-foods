# -*- coding: utf-8 -*-
import scrapy
import hashlib
from scrapy.http import Request
from ..database import StartUrl
from ..connection import db
from ..items import FoodNetworkRecipe
from ..loaders import FoodNetworkLoader

def url_hash(url):
    h = hashlib.sha256()
    h.update(url.encode('utf-8'))
    return h.hexdigest()


def url_clean(url):
    if '?' in url:
        url, params = url.split('?')
        return url
    return url

class FoodNetworkRecipesSpider(scrapy.Spider):
    name = 'food-network-recipes'
    allowed_domains = ['foodnetwork.com']
    start_urls = ['http://foodnetwork.com/']

    def start_requests(self):
        # overwride start_requests to get urls from db

        foodnetwork_starturls = (db.query(StartUrl).filter_by(s_id=2)
                            .limit(5))

        rqs = [ Request(url=start_url.url, callback=self.parse)
                for start_url in foodnetwork_starturls]

        return rqs


    def parse(self, response):

        foodnetwork_loader = FoodNetworkLoader(response=response, item=FoodNetworkRecipe())

        foodnetwork_loader.add_value('url', url_clean(response.url))
        foodnetwork_loader.add_value('url_hash', url_hash(url_clean(response.url)))

        foodnetwork_loader.add_xpath('name', '//h1[@class="o-AssetTitle__a-Headline"]/span/text()')

        foodnetwork_loader.add_value('date_published', None)

        foodnetwork_loader.add_xpath('ingredients', '//div[@class="o-Ingredients__m-Body"]/ul/li/label/text()')
        foodnetwork_loader.add_xpath('method', '//div[@class="o-Method__m-Body"]/p/text()')

        return foodnetwork_loader.load_item()
