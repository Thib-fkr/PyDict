# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Word_ID(Base):
    __tablename__ = 'word_id'

    word = Column(String, primary_key=true)

    french_id = relationship('French', uselist=False, back_populates='ref_word')

    english_id = relationship('English', uselist=False, back_populates='ref_word')

    dutch_id = relationship('Ducth', uselist=False, back_populates='ref_word')

    def __init__(self, word):
        self.word = word
