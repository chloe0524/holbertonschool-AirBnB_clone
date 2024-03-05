#!/usr/bin/python3
"""This module defines the 'BaseModel class'"""
# rajouter infos dans docstring ici maybe; à voir
import uuid
from datetime import datetime
import copy
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

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)

        # possibilité de ne mettre qu'une seule condition au lieu de deux ?
        # à voir
        if kwargs is not None:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.fromisoformat(
                    kwargs['created_at']
                )
            # possibilité de mettre "%Y-%m-%dT%H:%M:%S.%f" au lieu
            # de isoformat, à voir
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.fromisoformat(
                    kwargs['updated_at']
                )

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
        # je sais pas si utiliser copy ou deepcopy, à voir
        my_dict = copy.deepcopy(self.__dict__)
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
