#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    for item in a_dictionary.items():
        new_dict.update({item[0]: item[1] * 2})

    return new_dict
