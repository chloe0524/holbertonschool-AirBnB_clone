#!/usr/bin/python3
"""This module defines the FileStorage class"""

import json


class FileStorage():
    """This class serializes and deserializes 'JSON' files"""

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Returns all objects."""
        return self.__objects

    def new(self, obj):
        """Set in '__objects' the 'obj' with key <obj class name>.id"""
        key = ("{}.{}".format(type(obj).__name__, obj.id))
        self.__objects[key] = obj

    def save(self):
        """serialize '__objects' to the 'JSON' file"""

        jason_dico = dict()

        for key, value in self.__objects.items():
            jason_dico[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jason_dico, f)

    def reload(self):
        """Deserialize the 'JSON' file to '__objects'"""
        from models.base_model import BaseModel

        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
            for key, value in objects.items():
                class_name = value.pop('__class__', None)
                if class_name == 'BaseModel':
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
