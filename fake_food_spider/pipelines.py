# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FakeFoodSpiderPipeline(object):
    def process_item(self, item, spider):
        """
        Lets process a recipe item, we need to store it in the db
        """
        
        return item
