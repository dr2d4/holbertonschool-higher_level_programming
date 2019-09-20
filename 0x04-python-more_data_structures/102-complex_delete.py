#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    delete = []

    if value in a_dictionary.values():
        for item in a_dictionary.items():
            if item[1] == value:
                delete.append(item[0])

    for key in delete:
        a_dictionary.pop(key, 0)

    return a_dictionary