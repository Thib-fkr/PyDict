#
#
#
import os
import time
import logging
from Classes.baseTest import Session, engine, Base
from Functions.functionModule import updateRow, addRow, getColumnsNames,
                                     REL_getTrad, QUE_getTrad, dynamicQuery
# Loading classes to dodge error from getTableObject function due to dynamically created class...
# https://stackoverflow.com/questions/51296432/flask-sqlalchemy-db-model-decl-class-registry-values-and-db-metadata-tables-a
from Classes.languageClass import *


def name_value_parser(line:list, element:int, char:str = ':'):
    return (line[element].split(char)[elem_id] for elem_id in range(2))


def input_parser(user_input:list, debug=False, exit=False):
    """
    Format :
    --------

    Parameters :
    ------------
    user_input : (list)
    debug : (optional, bool)
    debug : (optional, bool)

    Output :
    --------
    infos : (dict)
    debug : (bool)
    exit : (bool)
    """
    # Initialize info data structure
    infos = {}

    # Iterate over each input the user made
    for line in user_input:
        line = line.split()
        action = line[0]

        # Check if there is a special keyword
        if action == 'help':
            print('help')
        elif action == 'exit':
            exit = True
        elif action == 'debug':
            debug = True
        else:
            # Create a 'action' section in the 'info' dict and store
            # the source language
            infos[action] = {}
            infos[action]['language'] = line[1]

        for info in range(2, len(line)):
            if action == 'add':
                name, value = name_value_parser(line, info)
                if name in ('word', 'ref'):
                    infos[action][name] = value
                else:
                    try:
                        infos[action]['other']
                    except KeyError:
                        infos[action]['other'] = {}
                    infos[action]['other'][name] = value

            elif action == 'look':
                try:
                    infos[action]['other']
                except KeyError:
                    infos[action]['other'] = {}
                name, value = name_value_parser(line, info)
                infos[action]['other'][name] = value

            elif action == 'trad':
                name, value = name_value_parser(line, info)
                if name == 'target':
                    infos[action][name] = value
                else:
                    try:
                        infos[action]['other']
                    except KeyError:
                        infos[action]['other'] = {}
                    infos[action]['other'][name] = value

            elif action == 'edit':
                try:
                    infos[action]['search']
                except KeyError:
                    infos[action]['search'] = {}
                try:
                    infos[action]['to_edit']
                except KeyError:
                    infos[action]['to_edit'] = {}

                if info == 2:
                    for values in line[info].split(','):
                        name, value = (values.split(':')[n] for n in range(2))
                        infos[action]['search'][name] = value
                else:
                    for values in line[info].split(','):
                        name, value = (values.split(':')[n] for n in range(2))
                        infos[action]['to_edit'][name] = value

            elif action == 'view':
                pass

    return infos, debug, exit


def start_display():
    """"""
    # License Messages etc :
    #
    #
    #
    #
    # credits()
    # term_width, term_height = os.terminal_size()

    start_message = """
    PYDICT TERMINAL APPLICATION
    by ~~"""
    print(start_message)


def help_display():
    """"""
    help_message_header = """
     __________________
    |How does it work ?|
    |__________________|"""

    help_message_body ="""
    Write the actions you want the program to perform in the bow below.
    To make the program perform the actions, write \"ex\"."""

    help_message_actions = """
    Add a word to a language's dictionnary :
    --> add <language> <word> <ref_word> [word_information]

    Look for a word in regard to given information :
    --> look <language> [word_information]

    Translate a word from a language to another :
    --> trad <source_language> <target_language> [word_information]

    ([word_information] -> info_1:value_1 info_2:value_2 info_3:value_3)


    Edit a specific word's information :
    --> edit <language> [word_current_information] [word_new_information]

    ([word_~_information] -> info_1:value_1,info_2:value_2,info_3:value_3)


    View :
    --> Not implemented yet

    Complete :
    --> Not implemented yet
    """
    print(help_message_header)
    print(help_message_body)
    print(help_message_actions)


def result_format(result:list):
    """"""
    length = max((len(element) for element in result))
    print('|'+ length*'=' + '|')
    for element in result:
        print('|'+ element + (length-len(element))*' ' + '|')


def main():
    start_display()
    session = Session()

    while True:
        user_input_list = []

        while True:
            user_input = input('$')

            if user_input == 'ex':
                break
            else:
                # If user_input not empty
                if not user_input in ('\n', ''):
                    # Add user's input without the \n
                    user_input_list.append(user_input[:len(user_input)])

        infos, debug, exit = input_parser(user_input_list)
        actions = (action for action in infos)


        logger = logging.getLogger(__name__)
        logging.basicConfig(
                filename='pydict_森.log', filemode='a',\
                format="[%(levelname)s]%(asctime)s : %(message)s",\
                level=logging.DEBUG)
        if debug:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)


        for action in actions:

            if action == 'help':
                help_display()

            if action == 'edit':
                updateRow(session,
                          infos[action]['language'],
                          infos[action]['search'],
                          infos[action]['to_edit'])

            if action == 'add':
                addRow(session,
                       infos[action]['language'],
                       infos[action]['word'],
                       infos[action]['ref'],
                       infos[action]['other'], addWID=True)

            if action == 'look':
                result_format(dynamicQuery(session,
                                           infos[action]['language'],
                                           infos[action]['other']))

            if action == 'trad':
                result_format(REL_getTrad(session,
                                          infos[action]['language'],
                                          infos[action]['target'],
                                          infos[action]['other']))

            if action == 'view':
                result_format(infos[action])

            if action == 'complete':
                result_format(infos[action])

        if exit:
            session.close()
            break

if __name__ == "__main__":
    main()