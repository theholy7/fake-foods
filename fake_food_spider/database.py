from sqlalchemy import Column, String, Integer, DateTime, Boolean
from database.connection import Base
from datetime import datetime


class StartUrlDb(Base):
    __tablename__ = 'start_urls'

    id = Column(Integer, primary_key=True)
    url = Column(String(1000))
    date = Column(DateTime)
    is_recipe = Column(Boolean)

    def __init__(self, id=None, url=None, date=datetime.utcnow(), is_recipe=False):
        self.id = id
        self.url = url
        self.date = date
        self.is_recipe = is_recipe

    def __repr__(self):
        return "<URL: url='%s', is_recipe='%s'>".format(self.url, self.is_recipe)
