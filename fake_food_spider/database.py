from sqlalchemy import Column, String, Integer, DateTime, Boolean
from .connection import Base
from datetime import datetime


class StartUrl(Base):
    __tablename__ = 'start_urls'

    id = Column(Integer, primary_key=True)
    url = Column(String(1000))
    url_hash = Column(String(100))
    name = Column(String(100))
    date = Column(DateTime, default=datetime.utcnow())
    is_recipe = Column(Boolean)
    s_id = Column(Integer)

    def __init__(self, id=None, name=None, url=None, url_hash=None, is_recipe=False):
        self.id = id
        self.url = url
        self.url_hash = url_hash
        self.name = name
        self.is_recipe = is_recipe

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
