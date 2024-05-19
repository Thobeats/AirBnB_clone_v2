#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128),
                  nullable=False)

    cities = relationship('City', cascade="all, delete", backref='states')

    @property
    def cities(self):
        """
        returns the list of City instances
        with state_id equals to the current
        State.id
        """
        from models import storage
        cities = []
        for key, obj in storage.all(City).items():
            if obj.state_id == self.id:
                cities.append(obj)
        return cities
