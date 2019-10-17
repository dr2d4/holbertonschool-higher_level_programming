#!/usr/bin/python3
"""
Count lines of a file
"""


def number_of_lines(filename=""):
    """
    Count lines of a file
    """

    with open(filename, encoding="utf-8") as f:
        return len(f.readlines())
