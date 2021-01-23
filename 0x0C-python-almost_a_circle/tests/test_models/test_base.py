#!/usr/bin/python3
"""Unittest for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""
    def test_A_no_argument(self):
        """no argument"""
        a = Base()
        self.assertEqual(1, a.id)

    def test_B_None_as_arg(self):
        """None as arg"""
        b = Base(None)
        self.assertEqual(2, b.id)

    def test_C_no_arg_multiple(self):
        """multiple no arg test"""
        c = Base()
        d = Base()
        e = Base()
        self.assertEqual(3, c.id)
        self.assertEqual(4, d.id)
        self.assertEqual(5, e.id)

    def test_id_0(self):
        """test with id 0"""
        f = Base(0)
        self.assertEqual(0, f.id)

    def test_id_neg(self):
        """test with negative id"""
        g = Base(-2)
        self.assertEqual(-2, g.id)
