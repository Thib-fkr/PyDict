#
#
#

from sqlalchemy.inspection import inspect

from Classes.idClass import Word_ID

# The next imports are only to be used for static typing
from sqlalchemy.orm.session import Session as SessionObject

# from sqlalchemy.sql.schema import Table as TableObject
# from sqlalchemy.engine.base import Engine as EngineObject
# from sqlalchemy.orm.state import InstanceState as InstanceObject
# from sqlalchemy.orm import Mapper as MapperObject

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
    from Classes.baseTest import engine

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
    from sqlalchemy import MetaData

    if tableExist(tableName):

        meta = MetaData()
        meta.reflect(bind=engine)

        for table in meta.sorted_tables:
            if table.name == tableName :

                return table
    else:
        raise ValueError

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
    from Classes.baseTest import Base

    for table in Base._decl_class_registry.values():
        if hasattr(table, '__table__') and table.__table__.fullname == tableName:

            return table

def getTableInstance_REL(obj, target):
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

    # return [rel.mapper.local_table \
    #       for rel in inspect(obj).mapper.relationships \
    #       if rel.mapper.class_ == target]

def getTableInstance_QUE(session:SessionObject, model:str, query:dict):
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
    return session.query(getTableObject(model)) \
                .filter_by(**query) \
                .one()

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

    # return [inspect(getTable(tableName)).c[col] for col in getColumnsNames(tableName) if if columnName == col]

def entryExist(session:SessionObject, model:str, query:dict):
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
    from sqlalchemy import literal

    q = session.query(getTable(model)).filter_by(**query)

    return session.query(literal(True)) \
                    .filter(q.exists()) \
                    .scalar()

    # return session.query(literal(True))\
    #               .filter(session.query(getTable(model)).filter_by(**query).exists())\
    #               .scalar()

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

    if entryExist(session, 'word_id', query):

        return session.query(Word_ID) \
                    .filter_by(**query) \
                    .one()
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
    return session.query(getTable(model)) \
                    .filter_by(**query) \
                    .all()

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
    from Classes.languageClass import Language

    if (not entryExist(session, 'word_id', {'word' : ref_word})) and addWID:

        WIDobj = Word_ID(ref_word)
        obj = Language.factory(tableName, word, WIDobj, **others)

        session.add(WIDobj)
        session.add(obj)

        session.commit()

    elif (not entryExist(session, 'word_id', {'word' : ref_word})) and (not addWID):
        raise IOError

    else:
        obj = Language.factory(tableName, word, getWordIDObject(session,'word_id', ref_word), **others)

        session.add(obj)
        session.commit()

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

    session.query(getTable(model)) \
            .filter_by(**query) \
            .update(values, synchronize_session=False)

def deleteRow(session:SessionObject, model:str, query:dict):
    """
    Delete a specific row
    Parameters :
    ------------
    session : SQLAlchemy session object (sqlalchemy.orm.session.Session)\n
    model : (str)\n
    query : (dict)\n
    """
    session.query(getTable(model)) \
            .filter_by(**query) \
            .delete()

################################################

def QUE_getTrad(session:SessionObject, baseLanguage:str, targetLanguage:str, query:dict):
    """
    Get the traduction of a word based on two queries.
    Parameters :
    ------------
    Outputs :
    ---------
    """

    wordID = dynamicQuery(session, baseLanguage, query)[0]['ref_word_id']

    info = {'ref_word_id' : wordID}

    return session.query(rel) \
                    .filter_by(**info) \
                    .all()

    # return session.query(rel)\
    #               .filter_by(**{'ref_word_id' : dynamicQuery(session, baseLanguage, query)[0]['ref_word_id']})\
    #               .all()

def REL_getTrad(session:SessionObject, baseLanguage:str, targetLanguage:str, query:dict):
    """
    Get the traduction of a word based of the relationships between the tables.
    Parameters :
    ------------
    Outputs :
    ---------
    """

    languageObject = getTableInstance_QUE(session, baseLanguage, query).ref_word
    rel = getTableInstance_REL(languageObject, getTableObject(targetLanguage))

    info = {'ref_word_id' : languageObject.id}

    return session.query(rel) \
                    .filter_by(**info) \
                    .all()

    # return session.query(getTableInstance_REL(languageObject, getTableObject(targetLanguage))) \
    #               .filter_by(**{'ref_word_id' : getTableInstance_QUE(session, baseLanguage, query).ref_word.id}) \
    #               .all()