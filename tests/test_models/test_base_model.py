#!/usr/bin/python3
"""
Unit tests for base model
"""
import unittest
import pep8
import inspect
import json
from models.base_model import BaseModel
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
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """
        Test that models/base_model.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for the presence of docstrings in all functions
        """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class
    """
    def setUp(self):
        """
        Setup the test
        """
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.b3 = BaseModel()
        self.tests = [self.b1, self.b2, self.b3]

    def test_uniq_id(self):
        """
        Test if IDs are always uniq
        """
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertNotEqual(self.b1.id, self.b3.id)
        self.assertNotEqual(self.b2.id, self.b3.id)

    def test_datetime_format(self):
        """
        Test datetime format
        """
        for base in self.tests:
            self.assertIsNotNone(base.created_at.year)
            self.assertIsNotNone(base.created_at.month)
            self.assertIsNotNone(base.created_at.day)
            self.assertIsNotNone(base.created_at.hour)
            self.assertIsNotNone(base.created_at.minute)
            self.assertIsNotNone(base.created_at.second)
            self.assertIsNotNone(base.created_at.microsecond)

    def test_creation_order(self):
        """
        Test if BaseModel order creation
        """
        self.assertGreaterEqual(self.b2.created_at.microsecond,
                                self.b1.created_at.microsecond)
        self.assertLessEqual(self.b1.created_at.microsecond,
                             self.b3.created_at.microsecond)
        self.assertGreaterEqual(self.b3.created_at.microsecond,
                                self.b2.created_at.microsecond)

    def test_right_datetime(self):
        """
        Test that datetime works
        """
        dateTime = datetime.now()
        test = BaseModel()
        self.assertEqual(dateTime.year, test.created_at.year)
        self.assertEqual(dateTime.month, test.created_at.month)
        self.assertEqual(dateTime.day, test.created_at.day)
        self.assertEqual(dateTime.hour, test.created_at.hour)
        self.assertEqual(dateTime.minute, test.created_at.minute)
        self.assertEqual(dateTime.second, test.created_at.second)

    def test__str__(self):
        """
        Test str method
        """
        for base in self.tests:
            v = "[BaseModel] ({}) {}\n".format(base.id, base.__dict__)
            with patch('sys.stdout', new=StringIO()) as fake_out:
                print(base)
                self.assertEqual(fake_out.getvalue(), v)

    def test_save_method(self):
        """Test save method"""
        for base in self.tests:
            prev_t = base.updated_at.microsecond
            self.assertLessEqual(prev_t, base.updated_at.microsecond)
        for base in self.tests:
            creation = base.created_at
            self.assertEqual(creation, base.created_at)

    def test_to_dict_method(self):
        """
        Test to_dict method
        """
        for base in self.tests:
            json = base.to_dict()
            self.assertEqual(type(json["__class__"]), str)
            self.assertEqual(type(json["updated_at"]), str)
            self.assertEqual(type(json["id"]), str)
            self.assertEqual(type(json["created_at"]), str)
            c = base.created_at
            e1 = "{}-{:02d}-{:02d}T\
                 {:02d}:{:02d}:{:02d}.{:06d}".format(c.year, c.month, c.day,
                                                     c.hour, c.minute,
                                                     c.second, c.microsecond)
            c = base.updated_at
            e2 = "{}-{:02d}-{:02d}T\
                 {:02d}:{:02d}:{:02d}.{:06d}".format(c.year, c.month, c.day,
                                                     c.hour, c.minute,
                                                     c.second, c.microsecond)
            self.assertEqual(json["updated_at"], e2)
            self.assertEqual(json["created_at"], e1)

    def test_arg_errors(self):
        """Test number of arguments"""
        with self.assertRaises(Exception):
            BaseModel(1, 2)
            self.b1.save(1, 2)
            self.b1.to_dict(1, 2)

    def test_kwargs(self):
        """Test kwargs"""
        for base in self.tests:
            json = base.to_dict()
            copy = BaseModel(**json)
            self.assertFalse(copy is base)
            self.assertEqual(copy.id, base.id)
            self.assertEqual(copy.__dict__, base.__dict__)
            self.assertEqual(copy.__class__.__name__, base.__class__.__name__)
            copy2 = BaseModel({})
            self.assertNotEqual(copy2.__dict__, base.__dict__)
