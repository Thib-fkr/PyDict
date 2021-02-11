# File containing a table that will allow the program to map words inbetween the different languages.
#
#

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Classes.base import Base

class Word_ID(Base):
    """
    Reference word in english used to map other words in different languages
    """

    # Table info
    __tablename__ = 'word_id'
    id = Column(Integer, primary_key=True)

    # Values
    word = Column(String)

    # Relationships
    french_word = relationship("French")
    english_word = relationship("English")
    dutch_word = relationship("Dutch")

    def __init__(self, word):
        self.word = word
