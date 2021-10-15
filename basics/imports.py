'''
In this exercise, you will need to print an alphabetically sorted list of
all functions in the re module, which contain the word find.
'''


import re


def find_re():
    find_list = []
    for find_str in dir(re):
        if 'find' in find_str:
            find_list.append(find_str)

    print(set(find_list))


if __name__ == '__main__':
    find_re()
    