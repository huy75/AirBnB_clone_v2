#!/usr/bin/python3
"""Defines unnittests for models/engine/db_storage.py."""
import pep8
import models
import MySQLdb
import unittest
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
from models import storage


class TestDBStorage(unittest.TestCase):
    """Unittests for testing the DBStorage class."""
    @classmethod
    def setUpClass(cls):
        """DBStorage testing setup.
        Instantiate new DBStorage.
        Fill DBStorage test session with instances of all classes.
        """
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="California")
            # cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="San_Francisco", state_id=cls.state.id)
            # cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="betty@holberton.com", password="betty")
            # cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="Lovely_place", number_rooms=3,
                              number_bathrooms=1,
                              max_guest=6, price_by_night=120,
                              latitude=37.773972, longitude=-122.431297)
            # cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Wifi")
            #cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="stellar")
            # cls.storage._DBStorage__session.add(cls.review)
            # cls.storage._DBStorage__session.commit()

    '''
    @classmethod
    def tearDownClass(cls):
        """DBStorage testing teardown.
        Delete all instantiated test classes.
        Clear DBStorage session.
        """
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            del cls.state
            del cls.city
            del cls.user
            del cls.place
            del cls.amenity
            del cls.review
            cls.storage._DBStorage__session.close()
            del cls.storage
    '''

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        resultd = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(resultd.total_errors, 0, "go fix pep8")
        """
        resultt = style.check_files(['tests/test_models/test_engine/\
        test_db_storage.py'])
        self.assertEqual(resultt.total_errors, 0, "go fix pep8")
        """

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "console.py needs a docstring")

    @unittest.skipIf(type(models.storage) == DBStorage,
                     "can't run if storage is file")
    def test_attributes_DBStorage(self):
        """Tests for class attributes"""
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'reload'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))

    @unittest.skipIf(type(models.storage) == DBStorage,
                     "can't run if storage is file")
    def test_all_DBStorage(self):
        """Tests for the all method"""
        state = State(name="California")
        storage.new(state)
        storage.save()
        key = '{}.{}'.format(type(state).__name__, state.id)
        dic = storage.all(State)
        self.assertTrue(key in dic.keys())
        state1 = State(name="Oregon")
        storage.new(state1)
        storage.save()
        key1 = '{}.{}'.format(type(state1).__name__, state1.id)
        dic1 = storage.all()
        self.assertTrue(key in dic1.keys())
        self.assertTrue(key1 in dic1.keys())
        u = User(email="scoot@noot", password="scootnoot")
        storage.new(u)
        storage.save()
        key2 = '{}.{}'.format(type(u).__name__, u.id)
        dic2 = storage.all(User)
        self.assertTrue(key2 in dic2.keys())
        self.assertFalse(key1 in dic2.keys())
        self.assertFalse(key in dic2.keys())
        self.assertFalse(key2 in dic.keys())

    # @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
    #                 "can't run if storage is file")

    def test_reload(self):
        """Test for reload()"""
        obj = DBStorage()
        self.assertTrue(obj._DBStorage__engine is not None)
        self.assertTrue(type(obj), DBStorage)

if __name__ == "__main__":
    unittest.main()
