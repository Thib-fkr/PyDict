# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:@localhost:5432/PYDICT', pool_pre_ping=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()