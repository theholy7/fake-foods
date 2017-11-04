from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# db settings
dbuser = 'fake_foodie'
dbpass = 'fake_food'
dbhost = 'localhost'
dbname = 'fake_foods'

engine = create_engine("postgres://%s:%s@%s/%s?charset=utf8&use_unicode=0"
                       % (dbuser, dbpass, dbhost, dbname),
                       echo=False,
                       pool_recycle=1800)

db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))
Base = declarative_base()
