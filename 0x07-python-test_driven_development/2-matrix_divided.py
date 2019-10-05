#!/usr/bin/python3
"""
Divides all elements of a matrix [[(int / float), *], *]
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix [[(int / float), *], *]

    Parameters:
        :param matrix: [[(int / float), *], *]
        :param div: (int / float)

    Raises:
        TypeError: if the matrix lists are not the same size
        TypeError: if any of the items is not (int / float)
        TypeError: if matrix is not a list of lists
        TypeError: if "div" is not a (int / float)
        ZeroDivisionError: if "div" equals 0

    Return:
        New matrix
    """

    errors = [
        'matrix must be a matrix (list of lists) of integers/floats',
        'Each row of the matrix must have the same size',
    ]

    # Check if "div" is not a (int / float) or div is 0
    if not isinstance(div, (int, float)) or div == 0:
        if not div:
            raise ZeroDivisionError('division by zero')

        raise TypeError('div must be a number')

    # Check if matrix is not list of lists
    if not isinstance(matrix, list) or not all(isinstance(l, list) for l in matrix):
        raise TypeError(errors[0])

    # Check if all items of a list are (int / float)
    are_numbers = map(lambda y: list(map(lambda x: isinstance(x, (int, float)), y)), matrix)
    are_numbers = all(map(lambda x: all(x), are_numbers))
    if not are_numbers:
        raise TypeError(errors[0])

    # Check if all the lists are the same size
    list_len = sum(map(lambda l: len(l), matrix))
    success_len = len(matrix) * len(matrix[0])
    if list_len != success_len:
        raise TypeError(errors[1])

    new_matrix = map(lambda y: list(map(lambda x: round(x / div, 2), y)), matrix)
    return list(new_matrix)
