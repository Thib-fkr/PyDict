# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class FrenchSy(Base):
    __tablename__ = 'french_synonyms'

    word = Column(Integer, primary_key=True)

    ref_synonym_id = Column(Integer, ForeignKey=('french.id'))

    ref_synonym = relationship('French', back_populates='french_synonyms')

    synonyms = Column(String)

    def __init__(self, synonyms, ref_synonym):
        self.synonyms = synonyms
        self.ref_synonym = ref_synonym

class EnglishSy(Base):
    __tablename__ = 'english_synonyms'

    word = Column(Integer, primary_key=True)

    ref_synonym_id = Column(Integer, ForeignKey=('english.id'))

    ref_synonym = relationship('english', back_populates='english_synonyms')

    synonyms = Column(String)

    def __init__(self, synonyms, ref_synonym):
        self.synonyms = synonyms
        self.ref_synonym = ref_synonym

class DutchSy(Base):
    __tablename__ = 'dutch_synonyms'

    word = Column(Integer, primary_key=True)

    ref_synonym_id = Column(Integer, ForeignKey=('dutch.id'))

    ref_synonym = relationship('Dutch', back_populates='dutch_synonyms')

    synonyms = Column(String)

    def __init__(self, synonyms, ref_synonym):
        self.synonyms = synonyms
        self.ref_synonym = ref_synonym