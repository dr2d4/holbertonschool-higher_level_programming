#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.__size = size

        if isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if not self.__size:
            raise ValueError("size must be >= 0")
