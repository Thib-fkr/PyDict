from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class French(Base):
    """"""
    __tablename__ = 'french'

    id = Column(Integer, primary_key=True)

    ref_word_id = Column(Integer, ForeignKey('word_id.id'))
    word = Column(String)
    definition = Column(String)
    gender = Column(String)
    pos = Column(String)

    # Relationships
    ref_word = relationship('Word_ID', back_populates='french', uselist=False)
    synonyms = relationship('FrenchSy')

    def __init__(self, word, definition, gender, pos, ref_word):
        self.word = word
        self.definition = definition
        self.gender = gender
        self.pos = pos
        self.ref_word = ref_word

class English(Base):
    """"""
    __tablename__ = 'english'

    id = Column(Integer, primary_key=True)

    ref_word_id = Column(Integer, ForeignKey('word_id.id'))
    word = Column(String)
    definition = Column(String)
    pos = Column(String)

    # Relationships
    ref_word = relationship('Word_ID', back_populates='english', uselist=False)
    synonyms = relationship('EnglishSy')

    def __init__(self, word, definition, pos, ref_word):
        self.word = word
        self.definition = definition
        self.pos = pos
        self.ref_word = ref_word

class Dutch(Base):
    """"""
    __tablename__ = 'dutch'

    id = Column(Integer, primary_key=True)

    ref_word_id = Column(Integer, ForeignKey('word_id.id'))
    word = Column(String)
    definition = Column(String)
    gender = Column(String)
    pos = Column(String)

    # Relationships
    ref_word = relationship('Word_ID', back_populates='dutch', uselist=False)
    synonyms = relationship('DutchSy')

    def __init__(self, word, definition, gender, pos, ref_word):
        self.word = word
        self.definition = definition
        self.gender = gender
        self.pos = pos
        self.ref_word = ref_word