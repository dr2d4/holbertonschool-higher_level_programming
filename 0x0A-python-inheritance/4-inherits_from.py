#!/usr/bin/python3
"""
Check if an object inherits a class
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits a class
    """
    if type(obj) == a_class:
        return False

    return isinstance(obj, a_class)
