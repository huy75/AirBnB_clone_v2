#!/usr/bin/python3
"""
Unit tests for base model
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


class TestState(unittest.TestCase):
    """
    Test the State class.
    """
