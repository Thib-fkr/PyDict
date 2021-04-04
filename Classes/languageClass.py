# File containing the objects that will store basic dictionnary data.
#
#

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Classes.baseTest import Base


class Language(object):
    """
    Class that is to be used to create instances of other classes by using
    a factory method.
    """

    @staticmethod
    def factory(type:str, word:str, ref_word:str, **kwargs):
        if type == 'french' :
            return French(word=word, ref_word=ref_word, **kwargs)
        elif type == 'dutch' :
            return Dutch(word=word, ref_word=ref_word, **kwargs)
        elif type == 'english' :
            return English(word=word, ref_word=ref_word, **kwargs)


class French(Base):
    """
    French language table

    Information to specify :
    ------------------------
    """
    # Table info
    __tablename__ = 'french'
    ref_word_id = Column(Integer, ForeignKey('word_id.id'), primary_key=True)

    # Values
    word = Column(String)
    phonetic = Column(String)
    pos = Column(String)
    gender = Column(String)
    source_info = Column(String)
    definition = Column(String)
    tags = Column(String)
    examples = Column(String)
    synonyms = Column(String)

    # Relationships
    ref_word = relationship('Word_ID', back_populates='french_word')

    def __init__(self,
                 ref_word,
                 word,
                 phonetic='[]',
                 pos='', gender='', source_info='', definition='',
                 tags=[], examples=[], synonyms=[]):

        self.ref_word = ref_word
        self.word = word
        self.phonetic = phonetic
        self.pos = pos
        self.gender = gender
        self.source_info = source_info
        self.definition = definition
        self.tags = tags
        self.examples = examples
        self.synonyms = synonyms


class English(Base):
    """
    English language table

    Information to specify :
    ------------------------
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
    ref_word = relationship('Word_ID', back_populates='english_word')
    #synonyms = relationship('EnglishSy',back_populates='ref_synonym')

    def __init__(self, word, ref_word, definition='', pos='', gender=''):
        self.word = word
        self.ref_word = ref_word
        self.definition = definition
        self.gender = gender


class Dutch(Base):
    """
    Dutch language table

    Information to specify :
    ------------------------
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
    ref_word = relationship('Word_ID', back_populates='dutch_word')
    #synonyms = relationship('DutchSy',back_populates='ref_synonym')

    def __init__(self, word, ref_word, definition='', gender='', pos=''):
        self.word = word
        self.ref_word = ref_word
        self.definition = definition
        self.gender = gender
        self.pos = pos
