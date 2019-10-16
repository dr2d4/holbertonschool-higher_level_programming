#!/usr/bin/python3
"""
Print all items of a list sorted
"""


class MyList(list):
    """
    Print all items of a list sorted
    """
    def print_sorted(self):
        print(sorted(self))
