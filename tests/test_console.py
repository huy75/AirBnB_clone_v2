#!/usr/bin/python3
"""
Test for console
Usage:
    To be used with the unittest module:
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_console.py"
"""
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
import pep8
import os
import sys
import json
import console
import tests
from console import HBNBCommand

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models import storage

classes = ["User", "State", "City", "Amenity", "Place", "Review"]


class TestConsole(unittest.TestCase):
    """ """
    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """at the end of the test this will tear it down"""
        del cls.HBNB

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def setUp(self):
        """ Sets up the mock stdin and stderr. """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create_session(self, server=None):
        """ Creates the cmd session. """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        resultc = style.check_files(["console.py"])
        self.assertEqual(resultc.total_errors, 0, 'go fix Pep8')
        resultt = style.check_files(['tests/test_console.py'])
        self.assertEqual(resultt.total_errors, 0, 'go fix Pep8')

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Test quit command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_EOF(self):
        """Test that EOF quits."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.HBNB.onecmd("EOF"))

    def test_create_errors(self):
        """Test create command errors."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create notaclass")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "Testing db")
    def test_create(self):
        """Test create command."""
        # Create console session.
        cons = self.create_session()

        # Tests all classes.
        for className in classes:
            # Test "create {} test='TEST'".
            with patch('sys.stdout', new=StringIO()) as Output:
                cons.onecmd('create {} test=\"TEST\"'.format(className))
                create_stdout = Output.getvalue().strip()
                create_stdout = '{}.{}'.format(className, create_stdout)
                self.assertTrue(create_stdout in storage.all())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "not for DB")
    def test_show(self):
        """Test show command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show notaclass")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show BaseModel xxx")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    '''
    def test_destroy(self):
        """Test destroy command input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy notaclass")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("destroy BaseModel xxx")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
    '''

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Testing db")
    def test_all(self):
        """Test all command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("all notaclass")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Testing db")
    def test_update(self):
        """Test update command input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update notaclass")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update User xxx")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())

if __name__ == "__main__":
    unittest.main()
