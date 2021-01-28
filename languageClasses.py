from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class French(Base):
    __tablename__ = 'french'

    word_id = Column(Integer, ForeignKey('word_id.id'), primary_key=True)
    ref_word = relationship('Word_ID', back_populates='french_id')

    synonyms = relationship('FrenchSy')

    word = Column(String)
    definition = Column(String)
    gender = Column(String)
    pos = Column(String)

    def __init__(self, word, definition, gender, pos):
        self.word = word
        self.definition = definition
        self.gender = gender
        self.pos = pos

class English(Base):
    __tablename__ = 'english'

    word_id = Column(Integer, ForeignKey('word_id.id'), primary_key=True)
    ref_word = relationship('Word_ID', back_populates='english_id')

    word = Column(String)
    definition = Column(String)
    pos = Column(String)

    def __init__(self, word, definition, pos):
        self.word = word
        self.definition = definition
        self.pos = pos

class Dutch(Base):
    __tablename__ = 'dutch'

    word_id = Column(Integer, ForeignKey('word_id.id'), primary_key=True)
    ref_word = relationship('Word_ID', back_populates='dutch_id')

    word = Column(String)
    definition = Column(String)
    gender = Column(String)
    pos = Column(String)

    def __init__(self, word, definition, gender, pos):
        self.word = word
        self.definition = definition
        self.gender = gender
        self.pos = pos