import scrapy
from ..items import ProxyItem


class ProxySpider(scrapy.Spider):
    name = 'proxy-spider'
    start_urls = ['https://free-proxy-list.net/anonymous-proxy.html']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
            'fake_food_spider.middlewares.RandomUserAgentMiddleware': 343 },
        'ITEM_PIPELINES' :{
            'fake_food_spider.pipelines.ProxyPipeline': 300},
    }

    def parse(self, response):

        for entry in response.xpath('//tr')[1:]:
            data = entry.xpath('./td/text()').extract()

            try:
                proxy = ProxyItem()
                proxy['ip'] = data[0]
                proxy['port'] = data[1]
                proxy['location'] = data[2]
                proxy['schema'] = 'https://' if data[6] == 'yes' else 'http://'
                yield proxy

            except IndexError as e:
                continue

