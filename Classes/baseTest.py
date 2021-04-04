# File containing the base object that has to be initialized in order to use
# the SQLalchemy's ORM.
#

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:@localhost:5432/PYDICTDB',
                        pool_pre_ping=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()