#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This is a unittest for the file 6-max_integer.py
    """

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test unordered list of integers"""
        unord = [1, 3, 4, 2]
        self.assertEqual(max_integer(unord), 4)

    def test_max_at_beginning(self):
        """Test maximum number at beginning"""
        max_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_beginning), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test for single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_floats(self):
        """Test floats"""
        float_list = [2.1, 3.5, 85.8, 12.6]
        self.assertEqual(max_integer(float_list), 85.8)

    def test_ints_and_floats(self):
        """Test ints and floats"""
        int_float_list = [2, 3.6, 1, 0.3]
        self.assertEqual(max_integer(int_float_list), 3.6)

    def test_strings(self):
        """Test strings"""
        string = "Favour"
        self.assertEqual(max_integer(string), 'v')

    def test_string_list(self):
        """Test a list of strings"""
        str_list = ["My", "name"]
        self.assertEqual(max_integer(str_list), "name")

    def test_empty_str(self):
        """Test empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
