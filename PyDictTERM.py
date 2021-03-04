#
#
#

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
    for line in user_input:

        line = line.split()
        infos[line[0]] = {}
        infos[line[0]]['language'] = line[1]
        if line[0] == 'help':
            pass
        elif line[0] == 'exit':
            exit = True
        elif line[0] == 'debug':
            debug = True

        for info in range(len(line)):
            if info in [0,1]:
                continue
            if line[0] in ['add', 'look']:
                name, value = name_value_parser(line, info)
                infos[line[0]][name] = value

            elif line[0] == 'edit':
                if info == 2:
                    for values in line[info].split(','):
                        name, value = name_value_parser(line, info)
                        infos[line[0]]['search'] = {}
                        infos[line[0]]['search'][name] = value
                else:
                    for values in line[info].split(','):
                        name, value = name_value_parser(line, info)
                        infos[line[0]]['to_edit'] = {}
                        infos[line[0]]['to_edit'][name] = value

            elif line[0] == 'view':
                pass
    return infos, debug, exit





    return actions, info, debug, exit


def main():
    print('')
    while True:
        user_input_list = []

        while True:
            user_input = input('$')
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