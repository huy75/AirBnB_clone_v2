#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60),
                primary_key=True,
                nullable=False)

    created_at = Column(DateTime,
                        nullable=False,
                        default=dt.utcnow())
    updated_at = Column(DateTime,
                        nullable=False,
                        default=dt.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = dt.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
            if self.id is None:
                setattr(self, 'id', str(uuid.uuid4()))
            now = dt.now()
            if self.created_at is None:
                self.created_at = now
            if self.updated_at is None:
                self.updated_at = now
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = dt.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """Deletes the current instance"""
        models.storage.delete(self)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = dt.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del(dictionary["_sa_instance_state"])
        return dictionary
