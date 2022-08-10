#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for max integer in a list"""

    def test_empty_list(self):
        """test if list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_list(self):
        """test on a list of integers"""
        self.assertEqual(max_integer([2, 4, 6, 1]), 6)
        self.assertEqual(max_integer([-3, -5, -7, -1]), -1)

    def test_float_list(self):
        """test on a list of floats"""
        self.assertEqual(max_integer([2.4, 1.32, 5.32, 6.213, 0.43]), 6.213)
        self.assertEqual(max_integer([-3.21, -1.33, -5.23, -0.12]), -0.12)

    def test_int_float(self):
        """test on a list of both int and floats"""
        self.assertEqual(max_integer([2.21, 4, 6.3, -7]), 6.3)

    def test_single(self):
        """test on a list of one element"""
        self.assertEqual(max_integer([8]), 8)


if __name__ == '__main__':
    unittest.main()
