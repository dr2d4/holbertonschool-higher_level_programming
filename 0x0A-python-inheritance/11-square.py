#!/usr/bin/python3
""" Class BaseGeometry """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class Rectangule """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("width", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
