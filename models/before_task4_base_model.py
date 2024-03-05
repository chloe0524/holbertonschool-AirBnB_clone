#!/usr/bin/python3
"""This module defines the BaseModel class."""

import uuid
from datetime import datetime
import copy


class BaseModel():
    """
    BaseModel class is the base class

    Attributes:

        id (str): unique UUID for each instance.
        created_at (datetime): datetime when instance was created.
        updated_at (datetime): datetime when instance was last updated.

    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel

        Args:

            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.fromisoformat(
                    kwargs['created_at']
                )
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.fromisoformat(
                    kwargs['updated_at']
                )

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Return a string representation BaseModel"""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def save(self):
        """Update the 'updated_at attribute' to the current 'datetime'"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation 'BaseModel'"""
        my_dict = copy.deepcopy(self.__dict__)
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
