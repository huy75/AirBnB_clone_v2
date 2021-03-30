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


class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class.
    """
