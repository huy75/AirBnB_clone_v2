#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        self.cities()

    @property
    def cities(self):
        lCities = []
        for city in models.storage.all(City):
            if self.id == city.state_id:
                lCities.append(city)
        return lCities
