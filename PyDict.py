# Main file of the PYDICT project
#
#
from Functions.functionModule import dynamicQuery, getTable, getColumns, existingEntryQuery
from Classes.baseTest import Session, engine, Base

session = Session()
query = {'word' : 'bonjour'}
print(type(existingEntryQuery(session, 'french', query)))
#print(type(dynamicQuery(session, 'french', query)))
