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
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation 'BaseModel'"""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def save(self):
        """Update the 'updated_at attribute' to the current 'datetime'"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation 'BaseModel'"""
        new_dict = self.__dict__.copy()

        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
