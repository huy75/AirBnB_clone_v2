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
        Test City class type attributes.
        """
        new_review = self.rev
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        idd = getattr(new_review, "id")
        t City class type attributes.reated_at = getattr(new_review, "created_at")
        updated_at = getattr(new_review, "updated_at")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
        self.assertIsInstance(idd, str)
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)
