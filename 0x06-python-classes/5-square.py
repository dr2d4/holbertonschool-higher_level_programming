#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def my_print(self):
        if not self.__size:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print('{}'. format('#'), end='')

            print()
