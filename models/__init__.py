#!/usr/bin/python3
"""
This module imports the storage type
based on the env value
"""
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
