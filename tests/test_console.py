#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
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
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            bm = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            us = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            st = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(bm, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all User")
            self.assertIn(us, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertIn(st, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            call = ('create State name="California"')
            self.HBNB.onecmd(call)
            st = f.getvalue().strip()
            ids = []
            ID = ''
            ID = str(f.getvalue())
            ids.append(ID[:-1])
            key = "State." + ids[0]
            dict = storage.all()[key]
            self.assertTrue('name' in dict.__dict__)
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            output = f.getvalue()
            self.assertIn(st, output)
            self.assertIn("'name': 'California'", output)

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

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Testing db")
    def test_all(self):
        """Test all command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("all notaclass")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

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
