import scrapy
from scrapy.crawler import CrawlerProcess

class ProxySpider(scrapy.Spider):
    name = 'proxy-spider'
    start_urls = ['https://free-proxy-list.net/anonymous-proxy.html']


    def parse(self, response):

        for entry in response.xpath('//tr')[1:]:
            data = entry.xpath('./td/text()').extract()

            try:
                proxy = dict()
                proxy['ip'] = data[0]
                proxy['port'] = data[1]
                proxy['location'] = data[2]
                proxy['schema'] = 'https://' if data[6] == 'yes' else 'http://'
                proxy['last_checked'] = data[7]
                yield proxy

            except IndexError as e:
                pass


if __name__ == 'main':

    process = CrawlerProcess()
    process.crawl(ProxySpider)
    process.start()
