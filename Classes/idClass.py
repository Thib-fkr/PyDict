# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Classes.base import Base

class Word_ID(Base):
    """
    Reference word in english used to map other words in different languages
    """

    # Table info
    __tablename__ = 'word_id'
    id = Column(Integer, primary_key=true)

    # Values
    word = Column(String)

    # Relationships
    french_word = relationship("French", uselist=False, back_populates="ref_word")
    english_word = relationship("English", uselist=False, back_populates="ref_word")
    dutch_word = relationship("Dutch", uselist=False, back_populates="ref_word")

    def __init__(self, word):
        self.word = word
