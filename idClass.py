# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Word_ID(Base):
    """"""
    __tablename__ = 'word_id'

    id = Column(Integer, primary_key=true)

    word = Column(String)

    # Relationships :
    french_word = relationship("French", back_populates="ref_word", uselist=False)
    english_word = relationship("English", back_populates="ref_word", uselist=False)
    dutch_word = relationship("Dutch", back_populates="ref_word", uselist=False)

    def __init__(self, word):
        self.word = word
