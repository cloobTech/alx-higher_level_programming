#!/usr/bin/python3
""" Testing for the Rectangle Class """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(1, 20)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def test_isinstance(self):
        self.assertIsInstance(self.r1, Base)

    def test_rect_init(self):
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r2.id, 1)

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
