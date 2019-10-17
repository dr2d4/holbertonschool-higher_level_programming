#!/usr/bin/python3
"""
Write content to file
"""


def write_file(filename="", text=""):
    """
    Write content to file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        written = f.write(text)

    return written
