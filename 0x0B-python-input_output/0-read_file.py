#!/usr/bin/python3
"""
Read file in utf-8  encoding
"""


def read_file(filename=""):
    """
    Read file in utf-8  encoding
    """

    with open(filename, encoding="utf-8") as f:
        print("".join(f.readlines()), end="")
