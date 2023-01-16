#!/usr/bin/python3
""" Testing for the Base Class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_initialization(self):
        base1 = Base()
        base2 = Base(12)
        base3 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 12)
        self.assertEqual(base3.id, 2)


if __name__ == '__main__':
    unittest.main()
