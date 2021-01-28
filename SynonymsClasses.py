# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class FrenchSy(Base):
    __tablename__ = 'french_synonyms'

    word = Column(String, ForeignKey('french.word'), primary_key=True)
    synonyms = Column(String)

    def __init__(self, synonyms):
        self.synonyms = synonyms