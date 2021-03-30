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
