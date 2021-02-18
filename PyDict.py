# Main file of the PYDICT project
#
#
from Functions.functionModule import dynamicQuery, getTable, getColumns, existingEntryQuery
from Classes.baseTest import Session, engine, Base
from Classes.languageClass import *
from Classes.idClass import *

session = Session()

query = {'word' : 'hello'}
print(session.query(Word_ID).filter_by(**query).one())
"""
print(session.query(Word_ID) \
    .join(French) \
    .filter_by(**query) \
    .all()[0].french_word.word)
"""

