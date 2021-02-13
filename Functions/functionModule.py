#
#
#
from Classes.base import Session, engine, Base

from Classes.idClass import Word_ID
from Classes.languageClass import French, English, Dutch
from Classes.synonymsClass import FrenchSy, EnglishSy, DutchSy

def tableExist(tableName):
    """
    Check if a table exist
    Parameters :
    ------------
    tableName : name of the table (str)

    Output :
    --------
    existance : whether the table exist or not (bool)
    """
    return engine.has_table(tableName)

def dynamicQuery(session, model, **kwargs):
    """"""
    return session.query(model).filter_by(**kwargs).all()
