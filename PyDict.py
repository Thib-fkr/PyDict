# Main file of the PYDICT project
#
#
import sys
import argparse


"""
session = Session()
print(session.query(Word_ID) \
    .join(French) \
    .filter_by(**query) \
    .all()[0].french_word.word)
"""
parser = argparse.ArgumentParser()
args = parser.parse_args()