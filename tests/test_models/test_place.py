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
    Testing Place class
    """
