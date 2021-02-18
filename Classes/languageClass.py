# File containing the objects that will store basic dictionnary data.
#
#

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Classes.baseTest import Base

class Language(Base):

    @staticmethod
    def factory(type, **kwargs):
        if type == 'French' :
            return French(**kwargs)
        elif type == 'Dutch' :
            return Dutch(**kwargs),
        elif type == 'English' :
            return English(**kwargs)

class French(Language):
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

    def __init__(self, word, ref_word, definition='', gender='', pos=''):
        self.word = word
        self.ref_word = ref_word
        self.definition = definition
        self.gender = gender
        self.pos = pos

class English(Language):
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
    gender = Column(String)

    # Relationships
    ref_word = relationship('Word_ID', uselist=False, back_populates='english_word')
    synonyms = relationship('EnglishSy')

    def __init__(self, word, ref_word, definition='', pos='', gender=''):
        self.word = word
        self.ref_word = ref_word
        self.definition = definition
        self.gender = gender


class Dutch(Language):
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

    def __init__(self, word, ref_word, definition='', gender='', pos=''):
        self.word = word
        self.ref_word = ref_word
        self.definition = definition
        self.gender = gender
        self.pos = pos