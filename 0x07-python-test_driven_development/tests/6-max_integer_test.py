#!/usr/bin/python3

import unittest
max_int = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """ Represents a  test class """

    def test_max(self):
        result = max_int([2, 4, 6, 3, 7, 8])
        self.assertEqual(result, 8)
