#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = [bool(not item % 2) for item in my_list]
    return (new_list)
