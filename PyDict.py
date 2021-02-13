# Main file of the PYDICT project
#
#


from Functions.functionModule import tableExist, dynamicQuery

from Classes.baseTest import Session, engine, Base

from Classes.idClass import Word_ID
from Classes.languageClass import French, English, Dutch
from Classes.synonymsClass import FrenchSy, EnglishSy, DutchSy

#Base.metadata.create_all(engine)
session = Session()
model = French
query = {'word' : 'bonjour'}

res = dynamicQuery(session, model, query)
for o in res:
    print(o.word)
    print(o.ref_word.english_word[0].word)
