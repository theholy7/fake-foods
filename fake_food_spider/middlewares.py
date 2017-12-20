# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from random import choice

from scrapy import Request, signals

proxies = [{'ip': 'http://62.144.211.124:8080',
            'banned': False,
            'usage_count': 0},
           {'ip': 'http://149.202.61.179:3128',
            'banned': False,
            'usage_count': 0}]


class ProxyMiddleware(object):
    # This is the class that manages the proxies
    # Get a request, add proxy data,
    # Send the request along

    def process_request(self, request, spider):
        # We get the request being created
        # and we add a proxy to it

        request.meta['proxy'] = choice([proxy['ip'] for proxy in proxies
                                        if not proxy['banned']])

        spider.logger.info("Proxy {} selected".format(request.meta['proxy']))


    def process_response(self, request, response, spider):

        if response.status == 403:
            for proxy in proxies:
                if request.meta['proxy'] in proxy.values():
                    proxy['banned'] = True

                    return request

        else:
            for proxy in proxies:
                if request.meta['proxy'] in proxy.values():
                    proxy['usage_count'] += 1
                    spider.logger.info("Proxy {} used {} times".format(request.meta['proxy'],
                                                                       proxy['usage_count']))

        return response


class FakeFoodSpiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
