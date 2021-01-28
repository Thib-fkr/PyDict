from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class French(Base):
    __tablename__ = 'french'

    id = Column(Integer, primary_key=True)

    word_id = Column(Integer, ForeignKey('word_id.id'))

    ref_word = relationship('Word_ID')
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

    id = Column(Integer, primary_key=True)

    word_id = Column(Integer, ForeignKey('word_id.id'))

    word = Column(String)
    definition = Column(String)
    pos = Column(String)

    def __init__(self, word, definition, pos):
        self.word = word
        self.definition = definition
        self.pos = pos

class Dutch(Base):
    __tablename__ = 'dutch'

    id = Column(Integer, primary_key=True)

    word_id = Column(Integer, ForeignKey('word_id.id'))

    word = Column(String)
    definition = Column(String)
    gender = Column(String)
    pos = Column(String)

    def __init__(self, word, definition, gender, pos):
        self.word = word
        self.definition = definition
        self.gender = gender
        self.pos = pos