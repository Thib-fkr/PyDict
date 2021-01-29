# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class FrenchSy(Base):
    """"""

    # Table info
    __tablename__ = 'french_synonyms'
    id = Column(Integer, primary_key=True)

    # Values
    synonyms = Column(String)
    ref_synonym_id = Column(Integer, ForeignKey=('french.id'))

    # Relationships
    ref_synonym = relationship('French', back_populates='french_synonyms')

    def __init__(self, synonyms, ref_synonym):
        self.synonyms = synonyms
        self.ref_synonym = ref_synonym

class EnglishSy(Base):
    """"""

    # Table info
    __tablename__ = 'english_synonyms'
    id = Column(Integer, primary_key=True)

    # Values
    synonyms = Column(String)
    ref_synonym_id = Column(Integer, ForeignKey=('english.id'))

    # Relationship
    ref_synonym = relationship('English', back_populates='english_synonyms')

    def __init__(self, synonyms, ref_synonym):
        self.synonyms = synonyms
        self.ref_synonym = ref_synonym

class DutchSy(Base):
    """"""

    # Table info
    __tablename__ = 'dutch_synonyms'
    word = Column(Integer, primary_key=True)

    # Values
    synonyms = Column(String)
    ref_synonym_id = Column(Integer, ForeignKey=('dutch.id'))

    # Relationship
    ref_synonym = relationship('Dutch', back_populates='dutch_synonyms')

    def __init__(self, synonyms, ref_synonym):
        self.synonyms = synonyms
        self.ref_synonym = ref_synonym