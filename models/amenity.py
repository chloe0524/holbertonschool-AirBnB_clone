#!/usr/bin/python3

"""Amenity module"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Represents a type of facility or feature that a place may have.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
