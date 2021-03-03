# Main file of the PYDICT project
#
#
import sys
import argparse
import logging
from Classes.baseTest import Session



def main():
    parser = argparse.ArgumentParser(description='', epilog='')

    # How to know how many nargs ?

    # I will re-write these help messages later
    parser.add_argument('language', dest='language', action='store',\
                        help='base language')

    parser.add_argument('-d','--debug', dest='debug', action='store_true',\
                        help='enable debug log in a log file')

    parser.add_argument('-e','--edit',type=str , metavar='info', dest='edit', action='append', nargs='+',\
                        help='edit information about a word')

    parser.add_argument('-a','--add',type=str , metavar='info',dest='add', action='append', nargs='+',\
                        help='add information about a word')

    parser.add_argument('-l','--look',type=str ,metavar='info', dest='look', action='append', nargs='+',\
                        help='look for a specific word coresponding to criterias')

    parser.add_argument('-v','--view',type=str ,metavar='info', dest='view', action='append', nargs='+',\
                        help='look for a list of word corresponding to some criterias')

    parser.add_argument('-c','--complete', dest='complete', action='store_true',\
                        help='indicate wherever the data is incomplete')

    args = parser.parse_args()
    session = Session()

    logger = logging.getLogger(__name__)
    if args.debug:
        logging.basicConfig(filename='pydict-debug.log', filemode='a',\
                            format="[%(levelname)s]%(asctime)s : %(message)s",\
                            level=logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    while True:
        u = input('input :')
        if args.edit:
            # PyDict.py BaseLanguage -e [targetLanguage,]
            # display available column for the target language
            # input with the wanted information
            pass

        if args.add:
            # PyDict.py english -a [ID, word:value, info:value, info:value, ..., 0/1]
            pass

        if args.look:
            # PyDict.py english -l [info:value, ...]
            pass

        if args.view:
            # PyDict.py english -v [info:value, ...]
            pass

        if args.complete:
            # PyDict.py english -c
            pass
        if u == 'exit':
            break


    session.close()

if __name__ == "__main__":
    sys.exit(main())