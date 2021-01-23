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
        self.assertEqual(2, a.id)
        self.assertEqual(3, b.id)

    # Argument number tests

    def test_not_enough_args(self):
        """not enough arguments"""
        with self.assertRaises(TypeError):
            a = Rectangle(1)

    def test_not_enough_args(self):
        """not enough arguments"""
        with self.assertRaises(TypeError):
            a = Rectangle()

    # Integer validation tests

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
