#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    Class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Init Variables
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return __dict__ attribute of a object
        """

        if not isinstance(attrs, list):
            return self.__dict__

        for var in attrs:
            if not isinstance(var, str):
                return self.__dict__

        my_dict = self.__dict__

        new_dict = {
            attr: my_dict for attr in attrs if attr in self.__dict__.keys()
        }

        return new_dict
