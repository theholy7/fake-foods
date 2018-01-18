from sqlalchemy import Column, String, Integer, DateTime, Boolean
from .connection import Base
from datetime import datetime

class Proxy(Base):
    __tablename__ = 'proxies'

    id = Column(Integer, primary_key=True)
    schema = Column(String(10), default='http://')
    ip = Column(String(20))
    port = Column(String(20))
    location = Column(String(20), default='--')
    is_banned = Column(Boolean, default=False)
    usage_count = Column(Integer, default=0)


    def __repr__(self):
        return "<Proxy: {}:{} - {}>".format(self.ip, self.port, self.location)

class StartUrl(Base):
    __tablename__ = 'start_urls'

    id = Column(Integer, primary_key=True)
    url = Column(String(1000))
    url_hash = Column(String(100))
    name = Column(String(100))
    date = Column(DateTime, default=datetime.utcnow())
    is_recipe = Column(Boolean)
    s_id = Column(Integer)
    scrape_count = Column(Integer, default=0)
    scrape_date = Column(DateTime)

    def __init__(self, id=None, name=None, url=None, url_hash=None,
                 is_recipe=False, s_id=0, scrape_count=0, scrape_date=None):
        self.id = id
        self.url = url
        self.url_hash = url_hash
        self.name = name
        self.is_recipe = is_recipe
        self.s_id = s_id
        self.scrape_count = scrape_count
        self.scrape_date = scrape_date

    def __repr__(self):
        return "<URL: name={}, url={}>".format(self.name, self.url)


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    url = Column(String(1000))
    url_hash = Column(String(100))
    date_collected = Column(DateTime, default=datetime.utcnow())

    name = Column(String(100))
    date_published = Column(DateTime)

    ingredients = Column(String(1000))
    method = Column(String(2000))



    def __init__(self, id=None, name=None, url=None, url_hash=None, date_published=None, ingredients=None, method=None):
        self.id = id
        self.url = url
        self.url_hash = url_hash
        self.name = name
        self.date_published = date_published

        self.ingredients = ingredients
        self.method = method

    def __repr__(self):
        return "<RECIPE: name={}, url={}>".format(self.name, self.url)
