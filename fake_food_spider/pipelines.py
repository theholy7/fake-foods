# -*- coding: utf-8 -*-



# Define your item pipelines here
#
from scrapy.exceptions import DropItem
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.exc import DatabaseError, DataError, IntegrityError

from .connection import db
from .database import StartUrl, Recipe, Proxy
from .items import FakeFoodStartURL, FakeFoodRecipe, ProxyItem


class ProxyPipeline(object):
    def process_item(self, item, spider):
        """
        Lets process a recipe item, we need to store it in the db
        """
        if isinstance(item, ProxyItem):
            return self.store_proxy(item, spider)
        elif isinstance(item, FakeFoodRecipe)\
                or isinstance(item, FakeFoodStartURL):
            return item


        return self.default(item, spider)

    def default(self, item, spider):
        spider.logger.info('Processing default pipeline')
        raise DropItem('Not implemented')

    def store_proxy(self, item, spider):
        # Check if proxy exists in DB
        exists = (db.query(Proxy)
                  .filter_by(ip=item['ip'])
                  .first())

        if exists:
            # If yes, skip it
            spider.logger.info('Skip already exists item {}'
                               .format(item['ip']))
            return item

        proxy = Proxy(**item)

        try:
            # try to add and commit changes to db
            db.add(proxy)
            db.commit()
        except (IntegrityError, DataError) as e:
            # rollback if failed to commit and log error
            db.rollback()
            spider.logger.error(str(e))
        return item


class FakeFoodSpiderPipeline(object):
    def process_item(self, item, spider):
        """
        Lets process a recipe item, we need to store it in the db
        """
        if isinstance(item, FakeFoodStartURL):
            return self.store_start_url(item, spider)
        elif isinstance(item, FakeFoodRecipe):
            return self.store_recipe(item, spider)
        # else:

        return self.default(item, spider)

    def default(self, item, spider):
        spider.logger.info('Processing default pipeline')
        raise DropItem('Not implemented')

    def store_start_url(self, item, spider):
        # Check if StartUrl exists in DB
        exists = (db.query(StartUrl)
                  .filter_by(url_hash=item['url_hash'])
                  .first())

        if exists:
            # If yes, skip it
            spider.logger.info('Skip already exists item {}'
                               .format(item['name']))
            return item

        start_url = StartUrl(**item)

        try:
            # try to add and commit changes to db
            db.add(start_url)
            db.commit()
        except (IntegrityError, DataError) as e:
            # rollback if failed to commit and log error
            db.rollback()
            spider.logger.error(str(e))
        return item

    def store_recipe(self, item, spider):
        # Check if StartUrl exists in DB
        exists = (db.query(Recipe)
                  .filter_by(url_hash=item['url_hash'])
                  .first())

        if exists:
            # If yes, skip it
            spider.logger.info('Skip already exists item {}'
                               .format(item['name']))
            return item

        recipe = Recipe(**item)

        try:
            # try to add and commit changes to db
            db.add(recipe)
            db.commit()
        except (IntegrityError, DataError) as e:
            # rollback if failed to commit and log error
            db.rollback()
            spider.logger.error(str(e))
        return item
