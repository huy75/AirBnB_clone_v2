#!/usr/bin/python3
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
import os.path
from models import storage
from os import path
"""
    UnitTest for the command line interpreter
"""


class TestConsole(unittest.TestCase):
    b = BaseModel()

    def setUp(self):
        FileStorage._FileStorage__objects = {}
    # if os.path.exists("file.json"):
    # os.remove("file.json")
    # def tearDown(self):
    #    if os.path.exists("file.json"):
    #        os.remove("file.json")
    """
        Create cmd
    """

    def test_create_with_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="San Francisco" \
            state_id="0001"')
        self.assertTrue(os.path.exists("file.json"))

    def test_create_with_one_false_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="San Francisco" \
            statedz="0001"')
        f = FileStorage()
        f.reload()
        with self.assertRaises(AttributeError) as cm:
            for k, v in f._FileStorage__objects.items():
                v.foo
        self.assertEqual("'City' object has no attribute 'foo'",
                         str(cm.exception))

    def test_create_with_one_good_arguments_with_space_in_name(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="San Francisco" \
            state_id="0001"')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.name, "San Francisco")

    def test_create_with_good_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="Paris" state_id="0001"')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.name, "Paris")
            self.assertEqual(v.state_id, "0001")

    def test_create_with_boolean_value_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name="My_little_house" \
            longitude=-122.431297')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.longitude, -122.431297)

    def test_create_with_name_And_underscore_value_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name="My_little_house"')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.name, "My little house")

    def test_create_with_integer_value_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name="My_little_house" \
            price_by_night=300')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.price_by_night, 300)
