from Classes.base import Session, engine, Base

from Classes.idClass import Word_ID
from Classes.languageClass import French, English, Dutch
from Classes.synonymsClass import FrenchSy, EnglishSy, DutchSy

Base.metadata.create_all(engine)

session = Session()

# Test goes here

session.commit()
session.close()