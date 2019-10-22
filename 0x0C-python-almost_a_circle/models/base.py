#!/usr/bin/python3
""" Base Class """

import json
import os


class Base:
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init Variables

        :param id: by new instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write JSON to file """

        list_objects = []
        if list_objs is None or len(list_objs) == 0:
            list_objects = []
        else:
            for i in list_objs:
                list_objects.append(i.to_dictionary())

        json_text = Base.to_json_string(list_objects)

        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(json_text)

    @staticmethod
    def from_json_string(json_string):
        """ Return a JSON from a string """

        if json_string is None or json_string is "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return new instance """

        new_instance = None

        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        if cls.__name__ == "Square":
            new_instance = cls(1)

        if new_instance is not None:
            new_instance.update(**dictionary)

        return new_instance

    @classmethod
    def load_from_file(cls):
        """ Load JSON from file """

        filename = "{}.json".format(cls.__name__)
        instance_list = []

        if os.path.isfile(filename):
            with open(filename) as f:
                instance_object = cls.from_json_string(f.read())

                for instance_dict in instance_object:
                    instance_list.append(cls.create(**instance_dict))

                return instance_list
        else:
            return []
