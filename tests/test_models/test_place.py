#!/usr/bin/python3
"""
Unit tests for place
"""
import unittest
import pep8
import inspect
import json
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from unittest.mock import patch
from io import StringIO
import os
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Test Place class
    """
   @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests
        """
        cls.base_funcs = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """
        Test that models/place.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for the presence of docstrings in all functions
        """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestPlace(unittest.TestCase):
    """
    Testing Place class.
    """
    state = State(name="California")
    city = City(state_id=state.id, name="San Francisco")
    user = User(email="john@dow.com", password="pwd")
    new_place = Place(user_id=user.id, city_id=city.id,
                      name="House 1", longitude=1.2, latitude=2.2,
                      description="A house", number_rooms=2,
                      number_bathrooms=1, max_guest=4,
                      price_by_night=100)

    def TearDown(self):
        pass

    def test_Place_inheritance(self):
        """
        Tests that the City class Inherits from BaseModel.
        """
        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        """
        Checks that the attribute exist.
        """
        self.assertTrue("city_id" in self.new_place.__dir__())
        self.assertTrue("user_id" in self.new_place.__dir__())
        self.assertTrue("description" in self.new_place.__dir__())
        self.assertTrue("name" in self.new_place.__dir__())
        self.assertTrue("number_rooms" in self.new_place.__dir__())
        self.assertTrue("max_guest" in self.new_place.__dir__())
        self.assertTrue("price_by_night" in self.new_place.__dir__())
        self.assertTrue("latitude" in self.new_place.__dir__())
        self.assertTrue("longitude" in self.new_place.__dir__())
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

    def test_type_longitude(self):
        """
        Test the type of longitude.
        """
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_latitude(self):
        """
        Test the type of latitude.
        """
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    def test_type_amenity(self):
        """
        Test the type of amenity_ids.
        """
        amenity = getattr(self.new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    def test_type_price_by_night(self):
        """
        Test the type of price_by_night.
        """
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_max_guest(self):
        """
        Test the type of max_guest.
        """
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_number_bathrooms(self):
        """
        Test the type of number_bathrooms.
        """
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_number_rooms(self):
        """
        Test the type of number_rooms.
        """
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_description(self):
        """
        Test the type of description.
        """
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    def test_type_name(self):
        """
        Test the type of name.
        """
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    def test_type_user_id(self):
        """
        Test the type of user_id.
        """
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_city_id(self):
        """
        Test the type of city_id.
        """
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)
        
    def test_type_id(self):
        """
        Test the type of id.
        """
        idd = getattr(self.new_place, "id")
        self.assertIsInstance(idd, str)

    def test_type_created_at(self):
        """
        Test the type of created_at.
        """
        created_at = getattr(self.new_place, "created_at")
        self.assertIsInstance(created_at, datetime)

    def test_type_updated_at(self):
        """
        Test the type of updated_at.
        """
        updated_at = getattr(self.new_place, "updated_at")
        self.assertIsInstance(updated_at, datetime)