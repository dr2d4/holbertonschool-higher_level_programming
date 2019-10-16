#!/usr/bin/python3
"""
First figure add
"""


class BaseGeometry:
    """
    base for all figures
    """
    def area(self):
        """
        Empty
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate numbers
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0.".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangles!
    """
    def __init__(self, width, height):
        """ Init Variables """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of a Rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ Return string """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
