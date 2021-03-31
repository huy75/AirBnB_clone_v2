#!/usr/bin/python3
"""
Unit tests for review
"""
import unittest
import pep8
import inspect
import json
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from unittest.mock import patch
from io import StringIO
import os
from datetime import datetime


class TestReviewDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of Review class
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests
        """
        cls.base_funcs = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """
        Test that models/review.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for the presence of docstrings in all functions
        """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestReview(unittest.TestCase):
    """
    Test the Review class.
    """
    state = State(name="California")
    city = City(state_id=state.id, name="San Francisco")
    user = User(email="john@dow.com", password="pwd")
    place = Place(user_id=user.id, city_id=city.id, name="House 1")
    rev = Review(place_id=place.id, user_id=user.id, text="Nice place")

    def test_Review_inheritance(self):
        """
        Tests that the Review class Inherits from BaseModel.
        """
        new_review = self.rev
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        """
        Test that Review class has place_id,
        user_id and text attributes.
        """
        new_review = self.rev
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_Review_attributes(self):
        """
        Test Review class type attributes.
        """
        new_review = self.rev
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        idd = getattr(new_review, "id")
        created_at = getattr(new_review, "created_at")
        updated_at = getattr(new_review, "updated_at")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
        self.assertIsInstance(idd, str)
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)
