#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv
storage_type = getenv('HBNB_TYPE_STORAGE')

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=False)
    number_rooms = Column(Integer,
                          default=0,
                          nullable=False)
    number_bathrooms = Column(Integer,
                              default=0,
                              nullable=False)
    max_guest = Column(Integer,
                       default=0,
                       nullable=False)
    price_by_night = Column(Integer,
                            default=0,
                            nullable=False)
    latitude = Column(Float,
                      nullable=False)
    longitude = Column(Float,
                       nullable=False)
    amenity_ids = []

    if storage_type == "db":
        reviews = relationship('Review', cascade="all, delete", backref="place")
    else:
        @property
        def reviews(self):
            """
            returns the list of that returns the list
            of Review instances with place_id
            equals to the current Place.id
            """
            from models import storage
            allReviews = []
            for key, obj in storage.all(Review).items():
                if obj.place_id == self.id:
                    allReviews.append(obj)
            return allReviews
