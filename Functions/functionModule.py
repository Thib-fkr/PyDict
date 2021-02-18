#
#
#

from sqlalchemy import MetaData
from sqlalchemy.inspection import inspect
from sqlalchemy import literal

from Classes.baseTest import Session, engine, Base
from Classes.languageClass import Language
from Classes.idClass import Word_ID

# The next imports are only to be used for static typing
from typing import Union

from sqlalchemy.orm.session import Session as SessionObject
from sqlalchemy.sql.schema import Table as TableObject
from sqlalchemy.engine.base import Engine as EngineObject


def getColumns(tableName:str):
    """
    Get all the available columns in a specific table
    Parameters :
    ------------
    tableName : name of the table (str)
    """
    return [column.name for column in inspect(getTable(tableName)).c]

def tableExist(tableName:str):
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

def getTable(tableName:str):
    """
    Get the SQLAlchemy table object by the provided name
    Parameters :
    ------------
    tableName : name of the table (str)

    Output :
    --------
    tableModel : SQLAlchemy table object (sqlalchemy.sql.schema.Table)

    Raise :
    -------
    ValueError : if the table does not exist
    """
    if tableExist(tableName):
        meta = MetaData()
        meta.reflect(bind=engine)

        for table in meta.sorted_tables:
            if table.name == tableName :
                return table
    else:
        raise ValueError

def dynamicQuery(session:SessionObject, model:TableObject, query:dict):
    """
    Allow to get informations from the database in a way that is more "user/develloper -friendly"
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : Table where you want to get the informations from (sqlalchemy.sql.schema.Table)\n
    query : How to filter wanted informations(dict)

    Outputs :
    ---------
    result : result of the query (list)
    Notes :
    -------
    The query (type:dictonnary) has to correspond to the following pattern :\n
    {
        column : value
    }\n
    (with both "column" and "value" being strings)
    """
    return session.query(getTable(model)).filter_by(**query).all()

def existingEntryQuery(session:SessionObject, model:TableObject, query:dict):
    """
    Check if an entry matches the info given as 'query'

    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : Table where you want to get the informations from (sqlalchemy.sql.schema.Table)\n
    query : How to filter wanted informations(dict)

    Output :
    --------
    entryExists : (bool)
    """
    q = session.query(getTable(model)).filter_by(**query)
    return session.query(literal(True)).filter(q.exists()).scalar()

def getWordIdObject(session:SessionObject, word:str):
    """
    Get the Word_ID object that corresponds to the given word

    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    word : (str)

    Output :
    --------
    Word_ID : (PYDICT.Classes.idClass.Word_ID)
    """
    query = {'word' : word}
    if existingEntryQuery(session, getTable('word_id'), query)
        return session.query(Word_ID).filter_by(**query).one()
    else:
        raise ValueError

# Maybe try to create a class with factory method and use it to make the function add_row ?

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
