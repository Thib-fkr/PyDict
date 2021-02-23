# Main file of the PYDICT project
#
#
import sys
import argparse
import logging

"""
session = Session()
print(session.query(Word_ID) \
    .join(French) \
    .filter_by(**query) \
    .all()[0].french_word.word)
"""

parser = argparse.ArgumentParser()

# How to know how many nargs ?

parser.add_argument('-d','--debug', dest='debug', action='store_true',\
                    help=)

parser.add_argument('-e','--edit', dest='edit', action='append', nargs=,\
                    help=)

parser.add_argument('-l','--look', dest='look', action='append', nargs=,\
                    help=)

parser.add_argument('-v','--view', dest='view', action='append',nargs =,\
                    help=)

parser.add_argument('-c','--complete', dest='complete', action='store_true',\
                    help=)

args = parser.parse_args()