#!/usr/bin/python3
"""
Unit tests for city
"""
import unittest
import pep8
import inspect
import json
from models.base_model import BaseModel
from models.city import City
from models.state import State
from unittest.mock import patch
from io import StringIO
import os
from datetime import datetime


class TestBaseDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of Base class
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests
        """
        cls.base_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """
        Test that models/base.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(City.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for the presence of docstrings in all functions
        """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestCity(unittest.TestCase):
    """
    Test the City class.
    """
    state = State(name="California")
    city = City(state_id=state.id, name="San Francisco")

    def test_City_inheritance(self):
        """
        tests that the City class Inherits from BaseModel.
        """
        new_city = self.city
        self.assertIsInstance(new_city, BaseModel)

    def test_City_attributes(self):
        """
        Test State class type attributes.
        """
        new_city = self.city
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())
        name_value = getattr(new_city, "id")
        self.assertIsInstance(name_value, str)
        name_value = getattr(new_city, "created_at")
        self.assertIsInstance(name_value, datetime)
        name_value = getattr(new_city, "updated_at")
        self.assertIsInstance(name_value, datetime)

    def test_type_name(self):
        """
        Test the type of name.
        """
        new_city = self.city
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        """
        Test the type of name.
        """
        new_city = self.city
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)
