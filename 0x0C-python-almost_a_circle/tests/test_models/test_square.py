#!/usr/bin/python3
"""test_square module"""
from unittest import TestCase, mock
from io import StringIO
import pep8
import inspect

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareDocs(TestCase):
    """Tests to check the documentation and style of Square class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.square_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_conformance_square(self):
        """Test that models/square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_square(self):
        """Test that tests/test_models/test_square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Square class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.square_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class Test_Square_basics(TestCase):
    """Test cases for Square initialization."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_empty(self):
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_Square_only_required(self):
        self.assertEqual(Square(2).id, 1)
        self.assertEqual(Square(4).id, 2)

    def test_Square_size_x(self):
        self.assertEqual(Square(2, 1).id, 1)
        self.assertEqual(Square(4, 2).id, 2)

    def test_Square_no_id(self):
        self.assertEqual(Square(2, 1, 2).id, 1)
        self.assertEqual(Square(4, 2, 1).id, 2)

    def test_Square_with_id(self):
        self.assertEqual(Square(2, 1, 2, 4).id, 4)
        self.assertEqual(Square(4, 2, 1, 2).id, 2)

    def test_size_get_set(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.size, 2)
        s.size = 42
        self.assertEqual(s.size, 42)

    def test_width_get(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.width, 2)

    def test_height_get(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.height, 2)

    def test_x_get(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.x, 1)

    def test_y_get(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.y, 2)


class Test_Square_values(TestCase):
    """Test cases for Square input, getter and setter values validation."""

    types = [
        None,
        "Betty Holberton",
        3.14,
        2j,
        ["Betty", "Holberton"],
        ("Betty", "Holberton"),
        range(42),
        {"first": "Betty", "last": "Holberton"},
        {"Betty", "Holberton"},
        frozenset({"Betty", "Holberton"}),
        True,
        b"Betty Holberton",
        bytearray(42),
        memoryview(bytes(42))
    ]

    def test_size_invalid_type(self):
        for type in self.types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(
                        TypeError, "width must be an integer"):
                    Square(type)

    def test_size_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-42)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_invalid_type(self):
        for type in self.types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(TypeError, "x must be an integer"):
                    Square(2, type)

    def test_x_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -42)

    def test_y_invalid_type(self):
        for type in self.types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(TypeError, "y must be an integer"):
                    Square(2, 0, type)

    def test_y_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 0, -42)


class Test_Square_area(TestCase):
    """Test cases for Square's area method."""

    def test_area_basic(self):
        self.assertEqual(Square(2).area(), 4)

    def test_area_with_args(self):
        with self.assertRaises(TypeError):
            Square(2).area(42)


class Test_Square_display(TestCase):
    """Test cases for Square's display method."""

    def test_display_basic(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2).display()
            self.assertEqual(output.getvalue(), '##\n##\n')

    def test_display_with_x(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2, 2).display()
            self.assertEqual(output.getvalue(), '  ##\n  ##\n')

    def test_display_with_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2, 0, 2).display()
            self.assertEqual(output.getvalue(), '\n\n##\n##\n')

    def test_display_with_x_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2, 2, 2).display()
            self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n')

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2).display(42)


class Test_Square_str(TestCase):
    """Test cases for Square's __str__ method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str_print(self):
        expected = "[Square] (42) 1/3 - 2"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            print(Square(2, 1, 3, 42), end='')
            self.assertEqual(output.getvalue(), expected)

    def test_str_str_method(self):
        expected = "[Square] (98) 3/1 - 4"
        self.assertEqual(Square(4, 3, 1, 98).__str__(), expected)

    def test_str_str(self):
        expected = "[Square] (1) 0/0 - 4"
        self.assertEqual(str(Square(4)), expected)

    def test_str_str_method_with_args(self):
        with self.assertRaises(TypeError):
            Square(2).__str__(42)


class Test_Square_update_with_args(TestCase):
    """Test cases for Square's update with *args method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_no_args(self):
        s = Square(2, 1, 2, 42)
        s.update()
        self.assertEqual(str(s), "[Square] (42) 1/2 - 2")

    def test_update_args_none_id(self):
        s = Square(2, 1, 2, 42)
        with self.assertRaises(TypeError):
            s.update(None)

    def test_update_args_id(self):
        s = Square(2, 1, 2, 42)
        s.update(24)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 2")

    def test_update_args_id_size(self):
        s = Square(2, 1, 2, 42)
        s.update(24, 10)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 10")

    def test_update_args_id_size_x(self):
        s = Square(2, 1, 2, 42)
        s.update(24, 10, 30)
        self.assertEqual(str(s), "[Square] (24) 30/2 - 10")

    def test_update_args_id_size_x_y(self):
        s = Square(2, 1, 2, 42)
        s.update(24, 10, 30, 40)
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def test_update_args_too_many_args(self):
        s = Square(2, 1, 2, 42)
        with self.assertRaises(TypeError):
            s.update(10, 10, 10, 10, 50, 60)

    def test_update_args_width_getter(self):
        s = Square(2, 1, 2, 42)
        with self.assertRaises(TypeError):
            s.update(10, 42, 10, 10, 50, 60)

    def test_update_args_height_getter(self):
        s = Square(2, 1, 2, 42)
        with self.assertRaises(TypeError):
            s.update(10, 42, 10, 10, 50, 60)

    def test_update_args_size_getter(self):
        s = Square(2, 1, 2, 42)
        with self.assertRaises(TypeError):
            s.update(10, 42, 10, 10, 50, 60)


class Test_Square_update_with_kwargs(TestCase):
    """Test cases for Square's update with **kwargs method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_kwargs_none_id(self):
        s = Square(2, 1, 2, 42)
        with self.assertRaises(TypeError):
            s.update(id=None)

    def test_update_kwargs_id(self):
        s = Square(2, 1, 2, 42)
        s.update(id=24)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 2")

    def test_update_kwargs_id_size(self):
        s = Square(2, 1, 2, 42)
        s.update(size=10, id=24)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 10")

    def test_update_kwargs_id_size_x(self):
        s = Square(2, 1, 2, 42)
        s.update(size=10, id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/2 - 10")

    def test_update_kwargs_id_size_x_y(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def test_update_kwargs_too_many_args(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, id=24, x=30, betty="holberton")
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def test_update_kwargs_mixed_too_many_args(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, betty="holberton", id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def test_update_kwargs_args_before(self):
        s = Square(2, 1, 2, 42)
        s.update(42, 42, y=10, x=30)
        self.assertEqual(str(s), "[Square] (42) 1/2 - 42")

    def test_update_kwargs_not_all_mixed(self):
        s = Square(2, 1, 2, 42)
        s.update(y=10, x=10, size=10)
        self.assertEqual(str(s), "[Square] (42) 10/10 - 10")

    def test_update_kwargs_only_wrong_keys(self):
        s = Square(2, 1, 2, 42)
        s.update(betty="holberton", holberton="betty")
        self.assertEqual(str(s), "[Square] (42) 1/2 - 2")


class Test_Square_to_dict(TestCase):
    """Test cases for Square's to_dictionary method."""

    def test_to_dictionary_basic(self):
        s = Square(2, 1, 2, 42)
        expected = {'size': 2, 'x': 1, 'y': 2, 'id': 42}
        self.assertDictEqual(s.to_dictionary(), expected)

    def test_to_dictionary_basic_with_args(self):
        with self.assertRaises(TypeError):
            Square(2, 1, 2, 42).to_dictionary(42)


if __name__ == "__main__":
    unittest.main()
