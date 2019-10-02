#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        error = 0

        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        error = 0

        if not isinstance(value, tuple):
            error = 1
        elif len(value) != 2:
            error = 2
        elif not all(isinstance(item, int) for item in value):
            error = 3
        elif value[0] < 0 or value[1] < 0:
            error = 4

        if error:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print('{}'. format(' '), end='')

                for j in range(self.__size):
                    print('{}'. format('#'), end='')

                print()
