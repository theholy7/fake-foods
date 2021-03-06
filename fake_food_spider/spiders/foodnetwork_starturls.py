# -*- coding: utf-8 -*-
import scrapy
import hashlib
from ..items import FakeFoodStartURL


def url_hash(url):
    h = hashlib.sha256()
    h.update(url.encode('utf-8'))
    return h.hexdigest()


def url_clean(url):
    if '?' in url:
        url, params = url.split('?')
        return url
    return url


class FoodNetworkStarturlsSpider(scrapy.Spider):
    name = 'food-network-starturls'
    spider_id = 2
    allowed_domains = ['foodnetwork.com']
    start_urls = ['http://www.foodnetwork.com/recipes/a-z/123']

    def parse(self, response):
        # collect all recipes from foodnetwork table of contents
        unformated_links = response.xpath('//ul[@class="o-IndexPagination__m-List"]//a/@href').extract()
        for u_link in unformated_links:
            if u_link.startswith('//'):
                url = 'http://' + u_link[2:]
                yield scrapy.Request(url=url, callback=self.parse_recipe_pages)

    def parse_recipe_pages(self, response):

        pagination_text = response.xpath('//section[@class="o-Pagination "]/ul//li//text()').extract()

        last_page = int(pagination_text[-2]) # Last item is 'Next', the one before it is the last page number

        for page in range(2, last_page+1):
            yield scrapy.Request(url=response.url + '/p/{}'.format(page), callback=self.parse_recipes)


    def parse_recipes(self, response):
        # check if Recipe name at the top
        # and return item if it is a recipe url
        recipe_selectors = response.xpath('//ul[@class="m-PromoList o-Capsule__m-PromoList"]//a')

        for recipe_selector in recipe_selectors:
            start_url_item = FakeFoodStartURL()
            start_url_item['is_recipe'] = True

            formated_url = 'http://' + recipe_selector.xpath('./@href').extract_first()[2:]

            start_url_item['url'] = url_clean(formated_url)
            start_url_item['name'] = recipe_selector.xpath('./text()').extract_first()
            start_url_item['url_hash'] = url_hash(url_clean(formated_url))
            start_url_item['s_id'] = self.spider_id

            yield start_url_item
