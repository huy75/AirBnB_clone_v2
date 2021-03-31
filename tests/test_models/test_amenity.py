#!/usr/bin/python3
"""
Unit tests for Amenity
"""
import unittest
import pep8
import inspect
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from unittest.mock import patch
from io import StringIO
import os
from datetime import datetime


class TestAmenityDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of Amenity class
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests
        """
        cls.base_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """
        Test that models/amenity.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for the presence of docstrings in all functions
        """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class.
    """
    am = Amenity(name="TV")
    am.save()

    def test_Amenity_inheritence(self):
        """
        Tests that the Amenity class Inherits from BaseModel.
        """
        new_amenity = self.am
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """
        Test that Amenity class had name attribute.
        """
        new_amenity = self.am
        self.assertTrue("name" in new_amenity.__dir__())
        self.assertEqual(new_amenity.name, "TV")

    def test_Amenity_attribute_type(self):
        """
        Test Amenity class type attributes.
        """
        new_amenity = self.am
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)
        name_value = getattr(new_amenity, "id")
        self.assertIsInstance(name_value, str)
        name_value = getattr(new_amenity, "created_at")
        self.assertIsInstance(name_value, datetime)
        name_value = getattr(new_amenity, "updated_at")
        self.assertIsInstance(name_value, datetime)
