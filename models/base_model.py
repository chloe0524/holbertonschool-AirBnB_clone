#!/usr/bin/python3

"""Module defining the BaseModel class."""
import uuid
from datetime import datetime

class BaseModel:
    """Class representing a base model with common attributes and methods."""

    def __init__(self):
        """Initialize a BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return f"[BaseModel] ({self.id}) {self.__dict__})"

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
