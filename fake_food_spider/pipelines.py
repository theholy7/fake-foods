# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.exc import IntegrityError, DataError, DatabaseError

from .connection import db
from .database import StartUrl
from .items import FakeFoodStartURL


class FakeFoodSpiderPipeline(object):
    def process_item(self, item, spider):
        """
        Lets process a recipe item, we need to store it in the db
        """
        if isinstance(item, FakeFoodStartURL):
            return self.store_start_url(item, spider)
        # elif isinstance(item, BBCGoodFoodItem):
        #    return self.store_object(item, spider)
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
