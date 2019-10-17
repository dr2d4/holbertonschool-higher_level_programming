#!/usr/bin/python3
"""
Append content to file
"""


def append_write(filename="", text=""):
    """
    Append content to file
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        written = f.write(text)

    return written
