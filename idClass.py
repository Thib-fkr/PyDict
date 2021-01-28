# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Word_ID(Base):
    __tablename__ = 'word_id'

    word = Column(String, primary_key=true)


    def __init__(self, word):
        self.word = word
