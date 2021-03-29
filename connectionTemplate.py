# File containing a template for the connection to a DB.
#
#

import time
from Classes.baseTest import Session, engine, Base
from Classes.idClass import Word_ID
from Classes.languageClass import French, English, Dutch
from Functions.functionModule import *


def main():
    session = Session()

"""
session = Session()
print(session.query(Word_ID) \
    .join(French) \
    .filter_by(**query) \
    .all()[0].french_word.word)
"""


"""
def main():
    Base.metadata.create_all(engine)

    # Initialize session
    session = Session()

    # -------------------------------------BEGIN------------------------------------------------------


    # Create wanted objects

    Hello = Word_ID('hello')
    Appel = Word_ID('appel')
    Banana = Word_ID('banana')
    Door = Word_ID('door')
    Desk = Word_ID('desk')
    Computer = Word_ID('computer')
    Smartphone = Word_ID('smartphone')

    hello = English('hello', Hello, definition='salutation', gender='neutral')
    appel = English('appel', Appel, definition='food', gender='neutral')
    banana = English('banana', Banana, definition='food', gender='neutral')
    door = English('door', Door, definition='room', gender='neutral')
    desk = English('desk', Desk, definition='room', gender='neutral')
    computer = English('computer', Computer, definition='computer', gender='neutral')
    smartphone = English('smartphone', Smartphone, definition='computer', gender='neutral')

    bonjour = French('bonjour',Hello , definition='salutation')
    pomme = French('pomme',Appel , definition='nourriture', gender='féminin')
    porte = French('porte',Door , definition='salle', gender='féminin')
    ordinateur = French('ordinateur',Computer, gender='masculin')
    telephone = French('téléphone',Smartphone, gender='masculin')

    sBonjour = FrenchSy('salut', bonjour)
    sHello = EnglishSy('Hi', hello)

    # Add them to session (one by one)
    session.add(Hello)
    session.add(Appel)
    session.add(Banana)
    session.add(Door)
    session.add(Desk)
    session.add(Computer)
    session.add(Smartphone)

    session.add(hello)
    session.add(appel)
    session.add(banana)
    session.add(door)
    session.add(desk)
    session.add(computer)
    session.add(smartphone)

    session.add(bonjour)
    session.add(pomme)
    session.add(porte)
    session.add(ordinateur)
    session.add(telephone)

    session.add(sBonjour)
    session.add(sHello)
    # --------------------------------------END-------------------------------------------------------

    # Commit and close the session

    session.commit()
    session.close()
    """

if __name__ == '__main__':
    main()