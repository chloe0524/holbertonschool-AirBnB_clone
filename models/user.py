#!/usr/bin/python3

"""module user"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    represents a registered user in the system.
    Contains email, password, first and last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""