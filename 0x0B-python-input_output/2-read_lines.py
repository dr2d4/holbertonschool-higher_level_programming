#!/usr/bin/python3
"""
Read X lines
"""


def read_lines(filename="", nb_lines=0):
    """
    Read X lines
    """

    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print("".join(f.readlines()), end="")
            return

        print("".join(f.readlines()[:nb_lines]), end="")
