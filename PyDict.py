# Main file of the PYDICT project
#
#
from Functions.functionModule import dynamicQuery, getTable, getColumns, existingEntryQuery, addRow, updateRow
from Classes.baseTest import Session, engine, Base
from Classes.languageClass import *
from Classes.idClass import *

session = Session()

query = {'definition' : 'from meedelen',
        'pos' : 'common noun'}
value = {'gender' : 'de'}
#session.query(Word_ID).filter_by(**query).one()
"""
print(session.query(Word_ID) \
    .join(French) \
    .filter_by(**query) \
    .all()[0].french_word.word)
"""
#addRow(session, 'dutch', 'mededeling', 'communication', query, addWID=True)
updateRow(session, 'dutch',query, value)
print(dynamicQuery(session, 'dutch', query))
