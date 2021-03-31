#!/usr/bin/python3
"""
Unit tests for user
"""
import unittest
import pep8
import inspect
import json
from models.base_model import BaseModel
from models.user import User
from unittest.mock import patch
from io import StringIO
import os
from datetime import datetime


class TestBaseDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of User class
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests.
        """
        cls.base_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """
        Test that models/user.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(User.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for the presence of docstrings in all functions
        """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestUser(unittest.TestCase):
    """
    Testing User class
    """
    user = User(first_name="John",
                last_name="Dow",
                email="john.dow@jd.com",
                password="psw")

    def test_User_inheritance(self):
        """
        tests that the User class Inherits from BaseModel
        """
        new_user = self.user
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attributes(self):
        """
        Test User class type attributes.
        """
        new_user = self.user
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_type_email(self):
        """
        Test the type of email
        """
        new = self.user
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    def test_type_first_name(self):
        """
        Test the type of first_name
        """
        new = self.user
        first_name = getattr(new, "first_name")
        self.assertIsInstance(first_name, str)

    def test_type_last_name(self):
        """
        Test the type of last_name
        """
        new = self.user
        last_name = getattr(new, "last_name")
        self.assertIsInstance(last_name, str)
