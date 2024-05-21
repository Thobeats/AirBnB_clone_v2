#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if HBNB_TYPE_STORAGE == "db":
        name = Column(String(128),
                      nullable=False)
        cities = relationship('City', cascade="all, delete",
                              backref='state',
                              order_by="City.name")
    else:
        name = ""

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

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
