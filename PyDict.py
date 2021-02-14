# Main file of the PYDICT project
#
#
from Functions.functionModule import dynamicQuery
from Classes.baseTest import Session, engine, Base

session = Session()
query = {'gender' : 'neutral'}
print(dynamicQuery(session, 'english', query))

