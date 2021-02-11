from Classes.base import Session, engine, Base

from Classes.idClass import Word_ID
from Classes.languageClass import French, English, Dutch
from Classes.synonymsClass import FrenchSy, EnglishSy, DutchSy

Base.metadata.create_all(engine)

# Initialize session
session = Session()

# -------------------------------------BEGIN------------------------------------------------------

# Create wanted objects

# Add them to session (one by one)

# --------------------------------------END-------------------------------------------------------

# Commit and close the session

session.commit()
session.close()