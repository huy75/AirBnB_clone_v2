#!/usr/bin/python3
"""
Unit tests for state
"""
import unittest
import pep8
import inspect
import json
from models.base_model import BaseModel
from models.state import State
from unittest.mock import patch
from io import StringIO
import os
from datetime import datetime


class TestStateDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of State class
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests
        """
        cls.base_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """
        Test that models/state.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for the presence of docstrings in all functions
        """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestState(unittest.TestCase):
    """
    Test the State class.
    """
    state = State(name="California")

    def test_State_inheritence(self):
        """
        Test State class inherits from BaseModel.
        """
        new_state = self.state
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """
        Test State class contains the attribute `name`.
        """
        new_state = self.state
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        """
        Test State class type attributes.
        """
        new_state = self.state
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
        name = getattr(new_state, "id")
        self.assertIsInstance(name, str)
        name = getattr(new_state, "created_at")
        self.assertIsInstance(name, datetime)
        name = getattr(new_state, "updated_at")
        self.assertIsInstance(name, datetime)
