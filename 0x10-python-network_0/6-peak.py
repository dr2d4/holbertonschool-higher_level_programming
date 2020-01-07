#!/usr/bin/python3
"""
    Function that finds a peak in a list of unsorted integers.
"""



def find_peak(list_of_integers):
    """
        function that finds a peak in a list of unsorted integers.
    """
    lista = sorted(list_of_integers)


    if lista:
        return lista[-1]