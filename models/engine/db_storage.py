#!/usr/bin/python3
"""
This module defines a class to manage DB storage for hbnb clone
"""
import json
import models
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.base_model import Base
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """
        This function starts the DB engine
        """
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')

        con = """mysql+mysqldb://{}:{}@{}/{}"""
        self.__engine = create_engine(con.format(HBNB_MYSQL_USER,
                                      HBNB_MYSQL_PWD,
                                      HBNB_MYSQL_HOST,
                                      HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name,
        if cls=None, query all types of objects
        """
        if cls is not None and cls.__name__ in classes:
            results = self.__session.query(classes[cls.__name__]).all()
            return {
                "{}.{}".format(result.__class__.__name__, result.id):
                result for result in results
            }
        else:
            all_objs = {}
            for key in classes.keys():
                objs = self.__session.query(key).all()
                for obj in objs:
                    objKey = "{}.{}".format(obj.__class__.__name__, obj.id)
                    all_objs[objKey] = obj
            return all_objs

    def new(self, obj):
        """
        Create new object class
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
