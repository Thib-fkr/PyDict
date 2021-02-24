#
#
#

from sqlalchemy import MetaData
from sqlalchemy.inspection import inspect
from sqlalchemy import literal

from sqlalchemy.orm import Mapper
from sqlalchemy.orm.state import InstanceState

from Classes.baseTest import Session, engine, Base
from Classes.languageClass import Language
from Classes.idClass import Word_ID

# The next imports are only to be used for static typing
from typing import Union
from Classes.languageClass import French as FrenchObject, English as EnglishObject, Dutch as DutchObject
from sqlalchemy.orm.session import Session as SessionObject
from sqlalchemy.sql.schema import Table as TableObject
from sqlalchemy.engine.base import Engine as EngineObject

def getTableObject(tableName:str):
    """
    Get table class object by it's name
    Parameters :
    ------------
    tableName : name of the table (str)
    Outputs :
    ---------
    table class : any of the table class objects initialized by the program ()
    """
    for table in Base._decl_class_registry.values():
        if hasattr(table, '__table__') and table.__table__.fullname == tableName:
            return table

def getRelationship(obj:Language.factory, target:Language.factory):
    """
    Get table instance based on the relationships
    Parameters :
    ------------
    obj :
    target :
    Outputs :
    ---------
    Notes :
    -------
    I might have to rewrite this function in a more efficient/simple way.
    Like using queries to get the object for example.
    """

    for rel in inspect(obj).mapper.relationships:
        if rel.mapper.class_ == target:
            return rel.mapper.local_table

def getColumnsNames(tableName:str):
    """
    Get all the available columns in a specific table
    Parameters :
    ------------
    tableName : name of the table (str)
    Outputs :
    ---------
    ColumnsName : (list)
    """
    return [column.name for column in inspect(getTable(tableName)).c]

def getColumnsObject(tableName:str, columnName:str):
    """"""
    for col in getColumnsNames(tableName):
        if columnName == col:
            inspec = inspect(getTable(tableName)).c
            return inspec[col]

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

def dynamicQuery(session:SessionObject, model:str, query:dict):
    """
    Allow to get informations from the database in a way that is more "user/develloper -friendly"
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : Table where you want to get the informations from (str)\n
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

def getLanguageObject(session:SessionObject, model:str, query:dict):
    """
    Get an instance of a table object
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : Wanted table object's name (str)\n
    query : How to filter wanted informations(dict)
    Outputs :
    ---------
    """
    return session.query(getTableObject(model)).filter_by(**query).one()

def existingEntryQuery(session:SessionObject, model:str, query:dict):
    """
    Check if an entry matches the info given as 'query'
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : Table where you want to get the informations from (str)\n
    query : How to filter wanted informations(dict)
    Output :
    --------
    entryExists : (bool)
    """
    q = session.query(getTable(model)).filter_by(**query)
    return session.query(literal(True)).filter(q.exists()).scalar()

def getWordIDObject(session:SessionObject, word:str):
    """
    Get the Word_ID object that corresponds to the given word
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : Table where you want to get the informations from (str)\n
    word : (str)
    Output :
    --------
    Word_ID : (PYDICT.Classes.idClass.Word_ID)
    """
    query = {'word' : word}
    if existingEntryQuery(session, 'word_id', query):
        return session.query(Word_ID).filter_by(**query).one()
    else:
        raise ValueError

def addRow(session:SessionObject, tableName:str, word:str, ref_word:str, others:dict, addWID=False):
    """
    Add a row to a table
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    tableName : name of the table (str)
    word : word you want to add (str)
    ref_word : reference word (str)
    others : informations about the word (dict)
    """
    if (not existingEntryQuery(session, 'word_id', {'word' : ref_word})) and addWID:

        WIDobj = Word_ID(ref_word)
        obj = Language.factory(tableName, word, WIDobj, **others)

        session.add(WIDobj)
        session.add(obj)

        session.commit()
        session.close()

    elif (not existingEntryQuery(session, 'word_id', {'word' : ref_word})) and (not addWID):
        raise IOError
    else:
        obj = Language.factory(tableName, word, getWordIDObject(session,'word_id', ref_word), **others)

        session.add(obj)
        session.commit()
        session.close()

def updateRow(session:SessionObject, model:str, query:dict, values:dict):
    """
    Update a specific row
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : (str)\n
    query : (dict)\n
    values : (dict)\n
    """
    # synchronize_session=False is here to prevent an error
    session.query(getTable(model)).filter_by(**query).update(values, synchronize_session=False)

def deleteRow(session:SessionObject, model:str, query:dict):
    """
    Delete a specific row
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : (str)\n
    query : (dict)\n
    """
    session.query(getTable(model)).filter_by(**query).delete()

################################################

def getTrad(session:SessionObject, baseLanguage:str, targetLanguage:str, query:dict):
    """
    
    Parameters :
    ------------
    Outputs :
    ---------
    """
    languageObject = getLanguageObject(session, baseLanguage, query).ref_word
    rel = getRelationship(languageObject, getTableObject(targetLanguage))
    info = {'ref_word_id' : languageObject.id}
    return session.query(rel).filter_by(**info).all()