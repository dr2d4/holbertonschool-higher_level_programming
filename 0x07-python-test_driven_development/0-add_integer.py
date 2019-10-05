#!/usr/bin/python3
"""
Adds two numbers (int/float)
"""


def add_integer(a, b=98):
    """
    Adds two numbers

    Parameters:
        a (int / float)
        b (int / float)

    Raises:
        TypeError: if a or b are not (integers / floats)

    Return:
        The sum two (integers/floats)
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return (int(a + b))
