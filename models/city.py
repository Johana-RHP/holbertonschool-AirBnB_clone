#!/usr/bin/python3
"""classes that inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits from BaseModel """
    state_id = ""
    name = ""
