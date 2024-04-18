#!/usr/bin/python3
"""
Write a class Amenity that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    A amenity class
    """
    __tablename__ = "amenities"

    name = Column(String(128),
                  nullable=False)

    place_amenities = relationship('Place',
                                   secondary=place_amenity,
                                   back_populates="amenities")
