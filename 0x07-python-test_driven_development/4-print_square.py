#!/usr/bin/python3
"""
Prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #

    Parameters:
        :param size: int

    Raises:
        TypeError: if size are not int

    Return:
        None
    """

    if not isinstance(size, (int, float, bool)):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    size = int(size)

    for _ in range(size):
        print('#' * size)
