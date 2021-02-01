from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class French(Base):
    """
    French language table

    Informations to specify :
    --------------
    word, 
    definition, 
    gender, 
    part-of-speech, 
    reference word
    """

    # Table info
    __tablename__ = 'french'
    ref_word_id = Column(Integer, ForeignKey('word_id.id'), primary_key=True)

    # Values
    word = Column(String)
    definition = Column(String)
    gender = Column(String)
    pos = Column(String)

    # Relationships
    ref_word = relationship('Word_ID', uselist=False, back_populates='french_word')
    synonyms = relationship('FrenchSy')

    def __init__(self, word, definition, gender, pos, ref_word):
        self.word = word
        self.definition = definition
        self.gender = gender
        self.pos = pos
        self.ref_word = ref_word

class English(Base):
    """
    English language table

    Informations to specify :
    --------------
    word, 
    definition, 
    part-of-speech, 
    reference word
    """

    # Table info
    __tablename__ = 'english'
    ref_word_id = Column(Integer, ForeignKey('word_id.id'), primary_key=True)

    # Values
    word = Column(String)
    definition = Column(String)
    pos = Column(String)

    # Relationships
    ref_word = relationship('Word_ID', uselist=False, back_populates='english_word')
    synonyms = relationship('EnglishSy')

    def __init__(self, word, definition, pos, ref_word):
        self.word = word
        self.definition = definition
        self.pos = pos
        self.ref_word = ref_word

class Dutch(Base):
    """
    Dutch language table

    Informations to specify:
    --------------
    word, 
    definition, 
    gender, 
    part-of-speech, 
    reference word
    """

    # Table info
    __tablename__ = 'dutch'
    ref_word_id = Column(Integer, ForeignKey('word_id.id'), primary_key=True)

    # Values
    word = Column(String)
    definition = Column(String)
    gender = Column(String)
    pos = Column(String)

    # Relationships
    ref_word = relationship('Word_ID', uselist=False, back_populates='dutch_word')
    synonyms = relationship('DutchSy')

    def __init__(self, word, definition, gender, pos, ref_word):
        self.word = word
        self.definition = definition
        self.gender = gender
        self.pos = pos
        self.ref_word = ref_word