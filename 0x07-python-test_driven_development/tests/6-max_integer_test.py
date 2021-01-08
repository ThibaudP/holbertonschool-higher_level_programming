#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """
        list is empty
        """
        list = []
        self.assertTrue(max_integer(list) == None)

    def test_no_list(self):
        """
        No list passed (should be the same as empty list)
        """
        self.assertTrue(max_integer() == None)

    def test_list_none(self):
        """
        list is None
        """
        self.assertRaises(TypeError)

    def test_equal_members(self):
        """
        All members of list are equal
        """
        list = [2, 2, 2, 2]
        self.assertTrue(max_integer(list) == 2)
    
    def test_single_member(self):
        """
        Only 1 member in the list
        """
        list = [1]
        self.assertTrue(max_integer(list) == 1)

    def test_negative_members(self):
        """
        negative members are added to the list
        """
        list = [1, 2, 3, -4]
        self.assertTrue(max_integer(list) == 3)

    def test_all_negative(self):
        """
        all negative members
        """
        list = [-1, -2, -3, -4]
        self.assertTrue(max_integer(list) == -1)

    def test_float(self):
        """
        add floats in the list
        """
        list = [1, 2, 3.5, 4.5]
        self.assertTrue(max_integer(list) == 4.5)

    def test_inf(self):
        """
        add infinity to the list
        """
        list = [1, 2, 3, float("inf")]
        self.assertTrue(max_integer(list) == float("inf"))