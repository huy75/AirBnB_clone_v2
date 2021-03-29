#!/usr/bin/python3
"""
Class db_storage
"""

from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

import os

class DBStorage:
    """
    The Db_Storage class
    """

    __engine = None
    __session = None
    classes = {
              'User': User, 'Place': Place,
              'State': State, 'City': City,
              'Amenity': Amenity, 'Review': Review
            }

    def __init__(self):
        """
        Constructor
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        d = {}
        if cls:
            liste = self.__session.query(cls).all()
            self.list_to_dict(liste, d)
        else:
            for row in self.classes:
                liste = self.__session.query(row).all()
                d = self.list_to_dict(liste, d)
        return d
                    

    def list_to_dict(self, liste, d):
        """
        Put the data of a list in a dictionnary
        """
        for obj in liste:
            key = obj.__class__.__name__ + '.' + obj.id
            d[key] = obj
        return d


    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
