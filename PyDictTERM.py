#
#
#
from Classes.baseTest import Session, engine, Base
import time, logging
from Functions.functionModule import updateRow, addRow, getColumnsNames, REL_getTrad, QUE_getTrad, dynamicQuery
# Loading classes to dodge Error from getTableObject function due to dynamically created class...
# https://stackoverflow.com/questions/51296432/flask-sqlalchemy-db-model-decl-class-registry-values-and-db-metadata-tables-a
from Classes.languageClass import *

def input_parser(user_input:list, debug=False, exit=False):
    """
    Format :
    --------

    Parameters :
    ------------

    Output :
    --------

    """
    def name_value_parser(line, info):
        return (line[info].split(':')[n] for n in range(2))

    infos = {}
    # Iterate over each input the user made
    for line in user_input:

        line = line.split()
        # Check if there is a special keyword
        if line[0] == 'help':
            print('help')
        elif line[0] == 'exit':
            exit = True
        elif line[0] == 'debug':
            debug = True
        else:

            # Create a 'action' section in the 'info' dict and store the source language
            infos[line[0]] = {}
            infos[line[0]]['language'] = line[1]

        for info in range(len(line)):
            if info in [0,1]:
                continue

            if line[0] == 'add':
                name, value = name_value_parser(line, info)
                if name in ['word', 'ref']:
                    infos[line[0]][name] = value
                else:
                    try:
                        infos[line[0]]['other']
                    except KeyError:
                        infos[line[0]]['other'] = {}
                    infos[line[0]]['other'][name] = value

            elif line[0] == 'look':
                try:
                    infos[line[0]]['other']
                except KeyError:
                    infos[line[0]]['other'] = {}
                name, value = name_value_parser(line, info)
                infos[line[0]]['other'][name] = value

            elif line[0] == 'trad':
                name, value = name_value_parser(line, info)
                if name == 'target':
                    infos[line[0]][name] = value
                else:
                    try:
                        infos[line[0]]['other']
                    except KeyError:
                        infos[line[0]]['other'] = {}
                    infos[line[0]]['other'][name] = value

            elif line[0] == 'edit':

                try:
                    infos[line[0]]['search']
                    infos[line[0]]['to_edit']
                except KeyError:
                    infos[line[0]]['search'] = {}
                    infos[line[0]]['to_edit'] = {}

                if info == 2:
                    for values in line[info].split(','):
                        name, value = (values.split(':')[n] for n in range(2))
                        infos[line[0]]['search'][name] = value
                else:
                    for values in line[info].split(','):
                        name, value = (values.split(':')[n] for n in range(2))
                        infos[line[0]]['to_edit'][name] = value

            elif line[0] == 'view':
                pass

    return infos, debug, exit

def result_format(result:list):
    """"""
    lenght = max([len(element) for element in result])
    print('|'+ lenght*'=' + '|')
    for element in result:
        print('|'+ element + (lenght-len(element))*' ' + '|')


def main():
    session = Session()
    print('')
    while True:
        user_input_list = []

        while True:
            user_input = input('$')
            if user_input == 'ex':
                break
            else:
                if user_input != '\n' and user_input != '':
                    user_input_list.append(user_input[:len(user_input)])

        infos, debug, exit = input_parser(user_input_list)
        actions = [a for a in infos]

        logger = logging.getLogger(__name__)
        if debug:
            logging.basicConfig(filename='pydict-debug.log', filemode='a',\
                                format="[%(levelname)s]%(asctime)s : %(message)s",\
                                level=logging.DEBUG)
            logger.setLevel(logging.DEBUG)

        for action in actions:

            if action == 'help':
                pass

            if action == 'edit':
                # PyDict.py BaseLanguage -e [targetLanguage,]
                updateRow(session, infos[action]['language'], infos[action]['search'], infos[action]['to_edit'])

            if action == 'add':
                # PyDict.py english -a [ID, word:value, info:value, info:value, ..., 0/1]
                addRow(session,infos[action]['language'],infos[action]['word'],infos[action]['ref'],infos[action]['other'], addWID=True)

            if action == 'look':
                # PyDict.py english -l [info:value, ...]
                result_format(dynamicQuery(session, infos[action]['language'], infos[action]['other']))

            if action == 'trad':
                # PyDict.py english -l [info:value, ...]
                result_format(REL_getTrad(session, infos[action]['language'], infos[action]['target'], infos[action]['other']))

            if action == 'view':
                # PyDict.py english -v [info:value, ...]
                result_format(infos[action])

            if action == 'complete':
                # PyDict.py english -c
                result_format(infos[action])
        if exit:
            session.close()
            break


if __name__ == "__main__":
    main()