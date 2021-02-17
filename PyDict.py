# Main file of the PYDICT project
#
#
from Functions.functionModule import dynamicQuery, getTable, getColumns
from Classes.baseTest import Session, engine, Base

session = Session()
query = {'gender' : 'neutral'}
print(type(dynamicQuery(session, 'english', query)))

