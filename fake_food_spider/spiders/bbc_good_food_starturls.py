# -*- coding: utf-8 -*-
import scrapy


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
            next_page_link = link.xpath('@href').extract_first()
            if '/recipes/' in next_page_link:
                yield response.urljoin(next_page_link))


    def parse_recipes(self, response):
        # check if Recipe name at the top
