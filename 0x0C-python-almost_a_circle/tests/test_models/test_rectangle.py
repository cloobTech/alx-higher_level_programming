#!/usr/bin/python3
""" Testing for the Rectangle Class """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):


    def test_init_id(self):
        r1 = Rectangle(2, 2)
        r2 = Rectangle(2, 2)
        self.assertEqual(r1.id, 1)

    def test_isinstance(self):
        r1 = Rectangle(2, 2)
        self.assertIsInstance(r1, Base)

    def test_width_data_type(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle("10", 2)

    def test_height_data_type_height(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, [2])

    def test_x_data_type(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, {6})

    def test_y_data_type(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 7, "a")

    def test_width_value(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, -2, 7)

    def test_height_value(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 0, 2, 7)

    def test_x_value(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 2, -5, -7)

    def test_y_value(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 2, -7, -3)
