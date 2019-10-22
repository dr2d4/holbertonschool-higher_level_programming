#!/usr/bin/python3
""" Test's for base class """

from unittest import TestCase
from models.base import Base


class TestBase(TestCase):
    """ Test's for base class methods """

    def test___init__(self):
        """ Test's for init method """

        self.assertTrue(Base.__init__.__doc__)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base("2").id, "2")
        self.assertEqual(Base().id, 2)

    def test_to_json_string(self):
        """ Test's for to_json_string method """

        json_string = Base().to_json_string({"id": 5191, "test": 1})
        self.assertEqual(type(json_string), type("test"))
        self.assertRegex(json_string, "\"id\": 5191")
        self.assertRegex(json_string, "\"test\": 1")

    def test_save_to_file(self):
        """ Test's for save_to_file method """

        self.assertTrue(Base.save_to_file.__doc__)

    def test_from_json_string(self):
        """ Test's for from_json_string method """

        json_string = Base().to_json_string({"id": 5191, "test": 1})
        self.assertTrue(Base.from_json_string.__doc__)
        resp = Base.from_json_string(json_string)
        self.assertEqual(resp["id"], 5191)
        self.assertEqual(resp["test"], 1)

    def test_create(self):
        """ Test's for create method """

        self.assertTrue(Base.create.__doc__)

    def test_load_from_file(self):
        """ Test's for load_from_file method """

        self.assertTrue(Base.load_from_file.__doc__)
