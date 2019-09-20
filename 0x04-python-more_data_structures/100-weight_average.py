#!/usr/bin/python3


def weight_average(my_list=[]):
    div = add = 0

    if not my_list:
        return 0

    for item in my_list:
        add += item[0] * item[1]
        div += item[1]

    return add / div
