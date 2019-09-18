#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if id >= 0 and idx < len(my_list):
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    else:
        return my_list