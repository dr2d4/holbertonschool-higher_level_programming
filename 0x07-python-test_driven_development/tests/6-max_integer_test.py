#!/usr/bin/python3
import unittest

"""
Unittest for max_integer
"""

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class TestMaxInteger
    """
    def test_max(self):
        """
        test max number in a list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """
        test empty list pass to max_integer
        """
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
