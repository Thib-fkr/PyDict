#
#
#

def input_parser(user_input):
    """
    Format :
    --------

    Parameters :
    ------------

    Output :
    --------

    """
    return action, info, debug


def main():
    print('')
    while True:
        user_input_list = []

        while True:
            user_input = input('')
            if user_input == 'ex\n':
                break
            else:
                user_input_list.append(user_input[:len(user_input)-1]) if user_input != '\n'


        actions, infos, debug, exit = input_list_parser(user_input_list)

        if debug:
            pass

        for action in actions:
            if action == 'help':
                pass

            if action == 'edit':
                # PyDict.py BaseLanguage -e [targetLanguage,]
                # display available column for the target language
                # input with the wanted information
                pass

            if action == 'add':
                # PyDict.py english -a [ID, word:value, info:value, info:value, ..., 0/1]
                pass

            if action == 'look':
                # PyDict.py english -l [info:value, ...]
                pass

            if action == 'view':
                # PyDict.py english -v [info:value, ...]
                pass

            if action == 'complete':
                # PyDict.py english -c
                pass
        if exit:
            break



if __name__ == "__main__":
    sys.exit(main())