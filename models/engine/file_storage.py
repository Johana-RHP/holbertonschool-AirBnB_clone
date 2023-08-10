#!/usr/bin/python3
""" Module FileStorage """

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ class File Storage serialize and deserialize JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Settings 4 FileStorage"""
        return self.__objects

    def new(self, obj):
        """Settings 4 FileStorage"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Settings 4 FileStorage"""
        d1 = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                d1[key] = value.to_dict()
            f.write(json.dumps(d1))

    def reload(self):
        """ Deserialize __objects from JSON file """

        dct = {'BaseModel': BaseModel,
               'User': User,
               'Place': Place,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Review': Review
               }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fd:
                obj_dict = json.load(fd)
                for key, value in obj_dict.items():
                    self.new(dct[value['__class__']](**value))
            return
