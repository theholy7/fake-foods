# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..database import StartUrl
from ..connection import db
from ..items import FakeFoodRecipe

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

        recipe = FakeFoodRecipe()

        recipe['url'] = url_clean(response.url)
        recipe['url_hash'] = url_hash(url_clean(response.url))


        recipe['name'] = response.xpath('//h1[@class="o-AssetTitle__a-Headline"]/span/text()').extract_first()

        recipe['date_published'] = None

        recipe['ingredients'] = response.xpath('//div[@class="o-Ingredients__m-Body"]/ul/li/label/text()').extract()
        recipe['method'] = response.xpath('//div[@class="o-Method__m-Body"]/p/text()').extract()


        pass
