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


class BbcGoodFoodStarturlsSpider(scrapy.Spider):
    name = 'bbc-good-food-starturls'
    spider_id = 1
    allowed_domains = ['bbcgoodfood.com']
    start_urls = ['https://www.bbcgoodfood.com/search/collections?query=']

    def parse(self, response):
        # collect all /recipes/ urls and make new request
        # check if they have the recipe title class
        # save url as recipe if recipe title class is in html
        # then save an is_recipe = True in the item
        content = response.xpath('//div[@class="view-content"]//h3/a/@href')

        for content_sel in content:
            content_link = content_sel.extract()
            self.logger.debug(content_link)
            if content_link:
                url = response.urljoin(content_link)

                if '/collection/' in url:
                    yield scrapy.Request(url=url, callback=self.parse)
                else:
                    yield scrapy.Request(url=url, callback=self.parse_recipes)

        #import pdb; pdb.set_trace()
        next_page = (response
                        .xpath('//a[@title="Go to next page"]/@href')
                        .extract_first())

        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url=url, callback=self.parse)


    def parse_recipes(self, response):
        # check if Recipe name at the top
        # and return item if it is a recipe url

        title_xpath = "//h1[@class='recipe-header__title']"
        title_selector = response.xpath(title_xpath)

        if title_selector:
            start_url_item = FakeFoodStartURL()
            start_url_item['is_recipe'] = True
            start_url_item['url'] = url_clean(response.url)
            start_url_item['name'] = (title_selector[0]
                                      .xpath('text()').extract_first())
            start_url_item['url_hash'] = url_hash(url_clean(response.url))
            start_url_item['s_id'] = self.spider_id

            yield start_url_item
