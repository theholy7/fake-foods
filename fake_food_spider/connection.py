from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .settings import DB_NAME, DB_USER, DB_HOST, DB_PASS

# db settings
dbuser = DB_USER
dbpass = DB_PASS
dbhost = DB_HOST
dbname = DB_NAME

engine = create_engine("postgres://%s:%s@%s/%s"
                       % (dbuser, dbpass, dbhost, dbname),
                       echo=False,
                       pool_recycle=1800)

db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))
Base = declarative_base()
