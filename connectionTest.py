from Classes.base import Session, engine, Base

from Classes.idClass import Word_ID
from Classes.languageClass import French, English, Dutch
from Classes.synonymsClass import FrenchSy, EnglishSy, DutchSy

Base.metadata.create_all(engine)

session = Session()

# Test goes here ------------------------------------------------------

# Reference word
hello = Word_ID('hello')
bye = Word_ID('bye')

# Word in a specific language
Ehello = English('hello','standart greeting', '', hello)
Fbonjour = French('bonjour', 'Salutation matinale ou dans le courant de l\'après midi', '', '', hello)
Dtotziens = Dutch('tot ziens', '', '', '', bye)

# Synonyms
FSbonjour = FrenchSy('salut',Fbonjour)

# add to session
session.add(hello)
session.add(bye)
session.add(Ehello)
session.add(Fbonjour)
session.add(Dtotziens)
session.add(FSbonjour)

session.commit()
session.close()