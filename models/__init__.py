#!/usr/bin/python3
"""
This module imports the storage type
based on the env value
"""
from os import getenv


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
