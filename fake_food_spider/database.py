from sqlalchemy import Column, String, Integer, DateTime, Boolean
from .connection import Base
from datetime import datetime


class StartUrl(Base):
    __tablename__ = 'start_urls'

    id = Column(Integer, primary_key=True)
    url = Column(String(1000))
    url_hash = Column(String(100))
    name = Column(String(100))
    date = Column(DateTime)
    is_recipe = Column(Boolean)

    def __init__(self, id=None, name=None, url=None,
                 url_hash=None, date=datetime.utcnow(), is_recipe=False):
        self.id = id
        self.url = url
        self.url_hash = url_hash
        self.name = name
        self.date = date
        self.is_recipe = is_recipe

    def __repr__(self):
        return "<URL: name={}, url={}>".format(self.name, self.url)
