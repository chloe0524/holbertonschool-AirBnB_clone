#!/usr/bin/python3

"""Module defining the BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class representing a base model with common attributes and methods."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance.
        If keyword arguments, attributes of the instance will be defined
        with the given values.
        'created_at' or 'updated_at' have to be in the following format :
        "%Y-%m-%dT%H:%M:%S.%f"

        If none, a new unique identifier will be created with UUID4,
        'created_at' and 'updated_at' will be defined with current datetime.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'update_at']:
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, val)
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return f"[BaseModel] ({self.id}) {self.__dict__})"

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()
        return self.updated_at

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        data = self.__dict__.copy()  # make a copy of the instance dictrionnary
        data['__class__'] = self.__class__.__name__  # class name
        data['created_at'] = self.created_at.isoformat()  # conversion to ISO
        data['updated_at'] = self.updated_at.isoformat()  # converts to ISO
        return data
