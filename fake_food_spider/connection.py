from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from scrapy.conf import settings

# db settings
dbuser = settings['DB_USER']
dbpass = settings['DB_PASS']
dbhost = settings['DB_HOST']
dbname = settings['DB_NAME']

engine = create_engine("postgres://%s:%s@%s/%s"
                       % (dbuser, dbpass, dbhost, dbname),
                       echo=False,
                       pool_recycle=1800)

db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))
Base = declarative_base()
