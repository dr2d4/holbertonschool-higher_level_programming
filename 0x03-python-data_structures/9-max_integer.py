#!/usr/bin/python3


def max_integer(my_list=[]):
    if (len(my_list) >= 0 and my_list is not None):
        max_num = 0

        for num in my_list:
            if num >= max_num:
                max_num = num

        return max_num
