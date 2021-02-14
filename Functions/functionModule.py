#
#
#
from sqlalchemy import MetaData

from sqlalchemy.inspection import inspect

from Classes.baseTest import Session, engine, Base

from Classes.languageClass import French, English, Dutch

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

def getTable(tableName=''):
    """
    Get the SQLAlchemy table object by the provided name
    """
    if tableExist(tableName):
        meta = MetaData()
        meta.reflect(bind=engine)

        for table in meta.sorted_tables:
            if table.name == tableName :
                return table
    else:
        raise ValueError('[+] the table {} does not exist'.format(tableName))

def dynamicQuery(session, model, query):
    """"""
    model = getTable(model)
    return session.query(model).filter_by(**query).all()

def getColumns(language):
    """"""
    columns = [column.name for column in inspect(string_to_language_object_mapper(language)).c]
    return columns

################################################

def getInfo(language, knownInfo, wantedInfo):
    """
    Get specific information about a word
    Parameters :
    ------------
    (session : SQLAlchemy session object)
    language : object from one of the classes in the languageClass file (listed in stringObjectMapper comments)
    knownInfo : info that are required to find the word you want info about (usually the word itself)
    wantedInfo : info you want to have about the specified word

    Output :
    --------
    info : the info you want (str)
    """
