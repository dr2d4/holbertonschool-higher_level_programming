#!/usr/bin/python3
"""
Two functions, one empty
"""


class BaseGeometry:
    """
    Two functions, one empty
    """
    def area(self):
        """
        Empty
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Not Empty function
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0.".format(name))
