#!/usr/bin/python3
"""Unittest for Rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""

    def setUp(self):
        """setUp method for Rectangle class"""
        Base._Base__nb_objects = 0

    # id tests

    def test_A_minimum_arguments(self):
        """minimum arguments"""
        a = Rectangle(1, 2)
        self.assertEqual(1, a.id)
        self.assertEqual(0, a.x)
        self.assertEqual(0, a.y)

    def test_B_two_instances_minimum_args(self):
        """Minimum arguments multiple instances"""
        a = Rectangle(1, 2)
        b = Rectangle(1, 2)
        self.assertEqual(1, a.id)
        self.assertEqual(2, b.id)

    # Argument number tests

    def test_not_enough_args(self):
        """not enough arguments"""
        with self.assertRaises(TypeError):
            a = Rectangle(1)

    def test_not_enough_args(self):
        """not enough arguments"""
        with self.assertRaises(TypeError):
            a = Rectangle()

    def test_too_many_args(self):
        """too many arguments"""
        with self.assertRaises(TypeError):
            a = Rectangle(8, 7, 0, 0, 12, 15)

    # Integer validation tests

    # width

    def test_width_float(self):
        """float as width"""
        with self.assertRaises(TypeError):
            a = Rectangle(1.5, 2)

    def test_width_list(self):
        """list as width"""
        with self.assertRaises(TypeError):
            a = Rectangle([1, 2], 2)

    def test_width_tuple(self):
        """tuple as width"""
        with self.assertRaises(TypeError):
            a = Rectangle((1, 2), 2)

    def test_width_set(self):
        """set as width"""
        with self.assertRaises(TypeError):
            a = Rectangle({1, 2}, 2)

    def test_width_dict(self):
        """dict as width"""
        with self.assertRaises(TypeError):
            a = Rectangle({"a": 1, "b": 2}, 2)

    def test_width_bool(self):
        """bool as width"""
        with self.assertRaises(TypeError):
            a = Rectangle(True, 2)

    def test_width_None(self):
        """None as width"""
        with self.assertRaises(TypeError):
            a = Rectangle(None, 2)

    def test_width_zero(self):
        """zero as width"""
        with self.assertRaises(ValueError):
            a = Rectangle(0, 2)

    def test_width_negative(self):
        """negative as width"""
        with self.assertRaises(ValueError):
            a = Rectangle(-5, 2)

    #  height

    def test_height_float(self):
        """float as height"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 1.5)

    def test_height_list(self):
        """list as height"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, [1, 2])

    def test_height_tuple(self):
        """tuple as height"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, (1, 2))

    def test_height_set(self):
        """set as height"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, {1, 2})

    def test_height_dict(self):
        """dict as height"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, {"a": 1, "b": 2})

    def test_height_bool(self):
        """bool as height"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, True)

    def test_height_None(self):
        """None as height"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, None)

    def test_height_zero(self):
        """zero as height"""
        with self.assertRaises(ValueError):
            a = Rectangle(1, 0)

    def test_height_negative(self):
        """negative as height"""
        with self.assertRaises(ValueError):
            a = Rectangle(1, -5)

    #  x

    def test_x_float(self):
        """float as x"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 1.5)

    def test_x_list(self):
        """list as x"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, [1, 2])

    def test_x_tuple(self):
        """tuple as x"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, (1, 2))

    def test_x_set(self):
        """set as x"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, {1, 2})

    def test_x_dict(self):
        """dict as x"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, {"a": 1, "b": 2})

    def test_x_bool(self):
        """bool as x"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, True)

    def test_x_None(self):
        """None as x"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, None)

    def test_x_zero(self):
        """zero as x"""
        a = Rectangle(1, 2, 0)
        self.assertEqual(0, a.x)

    def test_x_negative(self):
        """negative as x"""
        with self.assertRaises(ValueError):
            a = Rectangle(1, 2, -5)

    #  y

    def test_y_float(self):
        """float as y"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 1.5)

    def test_y_list(self):
        """list as y"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 1, [1, 2])

    def test_y_tuple(self):
        """tuple as y"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 1, (1, 2))

    def test_y_set(self):
        """set as y"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 1, {1, 2})

    def test_y_dict(self):
        """dict as y"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_y_bool(self):
        """bool as y"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 1, True)

    def test_y_None(self):
        """None as y"""
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 1, None)

    def test_y_zero(self):
        """zero as y"""
        a = Rectangle(1, 2, 1, 0)
        self.assertEqual(0, a.y)

    def test_y_negative(self):
        """negative as y"""
        with self.assertRaises(ValueError):
            a = Rectangle(1, 2, 1, -5)

# TODO:
# - tests for display
# - tests for update
