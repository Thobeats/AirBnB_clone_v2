#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv
storage_type = getenv('HBNB_TYPE_STORAGE')
place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=True))


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
                         nullable=True)
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
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    amenity_ids = []

    if storage_type == 'db':
        reviews = relationship('Review', cascade="all, delete", backref="place")

        amenities = relationship('Amenity',
                                secondary=place_amenity,
                                back_populates='place_amenities',
                                viewonly=False)
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

        @property
        def amenities(self):
            """
            Get amenities from file storage
            """
            return self.__amenity_ids

        @amenities.setter
        def amenities(self):
            """
            Set the amenity ids
            """
            from models import storage
            from models.amenity import Amenity

            amenities = storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.place_id == self.id:
                    self.amenity_ids.append(amenity)
