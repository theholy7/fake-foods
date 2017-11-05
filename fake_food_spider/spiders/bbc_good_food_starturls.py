# -*- coding: utf-8 -*-
import scrapy
import hashlib
from ..items import FakeFoodStartURL


def url_hash(url):
    h = hashlib.sha256()
    h.update(url.encode('utf-8'))
    return h.hexdigest()


class BbcGoodFoodStarturlsSpider(scrapy.Spider):
    name = 'bbc-good-food-starturls'
    allowed_domains = ['bbcgoodfood.com']
    start_urls = ['http://bbcgoodfood.com/']

    def parse(self, response):
        # collect all /recipes/ urls and make new request
        # check if they have the recipe title class
        # save url as recipe if recipe title class is in html
        # then save an is_recipe = True in the item

        for link in response.xpath('//a'):
            next_page_link = link.xpath('@href').extract_first(default='')
            if '/recipes/' in next_page_link:
                url = response.urljoin(next_page_link)
                yield scrapy.Request(url=url, callback=self.parse_recipes)

    def parse_recipes(self, response):
        # check if Recipe name at the top
        # and return item if it is a recipe url

        title_xpath = "//h1[@class='recipe-header__title']"
        title_selector = response.xpath(title_xpath)

        if title_selector:
            start_url_item = FakeFoodStartURL()
            start_url_item['is_recipe'] = True
            start_url_item['url'] = response.url
            start_url_item['name'] = (title_selector[0]
                                      .xpath('text()').extract_first())
            start_url_item['url_hash'] = url_hash(response.url)

            yield start_url_item

        # find all other recipe links in that recipe page
        for link in response.xpath('//a'):
            next_page_link = link.xpath('@href').extract_first(default='')
            if '/recipes/' in next_page_link:
                url = response.urljoin(next_page_link)
                yield scrapy.Request(url=url, callback=self.parse_recipes)
