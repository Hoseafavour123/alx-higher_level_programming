#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ This is a unittest for the file 6-max_integer.py
    """

    def setUp(self):
        """ Initialising test cases to be used
        """

        self.list_1 = [1, 3, 4, 2]
        self.list_2 = [1.2, 6.7, 19.3, 5.53, 15.9]
        self.list_3 = [7, 3, 'hello', True, 6]

    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(self.list_1), 4)
        self.assertEqual(max_integer(self.list_2), 19.3)

        self.assertRaises(TypeError, max_integer, self.list_3)

if __name__ == "__main__":
    unittest.main()
