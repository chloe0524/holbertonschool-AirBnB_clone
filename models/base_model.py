#!/usr/bin/python3
"""This module defines the 'BaseModel class'"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    'BaseModel class' is the base 'class'

    Attributes:

        id (str): unique UUID for each instance
        created_at (datetime): datetime when instance was created
        updated_at (datetime): datetime when instance was last updated

    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new 'BaseModel'

        Args:

            *args (any): unused
            **kwargs (dict): Key/value pairs of attributes
        """

        if kwargs:
            # If keyword arguments are provided, set attributes accordingly
            for key, value in kwargs.items():
                # If key is "__class__", skip it
                if key == "__class__":
                    continue
                # If key is "created_at" or "updated_at"
                # convert value to datetime object
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                # Set attribute
                setattr(self, key, value)
        else:
            # If no keyword arguments are provided:
            # initialize with default values
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Add instance to storage
            storage.new(self)

    def __str__(self):
        """Return a string representation 'BaseModel'"""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def save(self):
        """Update the 'updated_at attribute' to the current 'datetime'"""
        self.updated_at = datetime.now()
        # Save changes to storage
        storage.save()

    def to_dict(self):
        """Return a dictionary representation 'BaseModel'"""
        # Create a copy of the instance's dictionary
        new_dict = self.__dict__.copy()

        # Add "__class__" key with class name
        new_dict["__class__"] = self.__class__.__name__
        # Convert created_at and updated_at attributes to ISO format strings
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
