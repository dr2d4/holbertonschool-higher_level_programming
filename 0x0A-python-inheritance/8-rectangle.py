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
    First class inherited
    """
    def __init__(self, width, height):
        """
        Call validate numbers
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
