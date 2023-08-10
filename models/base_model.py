#!/usr/bin/python3
"""BaseModel class"""


import json
import uuid
import models
import datetime


class BaseModel:
    """BaseModel attributes n methods"""
    def __init__(self, *args, **kwargs):
        """BaseModel attributes n methods"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for keys, value in kwargs.items():
                if keys == "__class__":
                    continue
                if keys == 'id':
                    self.id = value
                elif keys == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif keys == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
                else:
                    setattr(self, keys, value)

    def __str__(self):
        """ Type method __str__ """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Type method save """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Type method to_dict """
        rt_dict = self.__dict__.copy()
        rt_dict["created_at"] = self.created_at.isoformat()
        rt_dict["updated_at"] = self.updated_at.isoformat()
        rt_dict["__class__"] = self.__class__.__name__
        return rt_dict
