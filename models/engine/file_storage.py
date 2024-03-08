#!/usr/bin/python3
import json
import os

""" module file_storage"""


class FileStorage:
    """
    This class represents a file storage
    system for storing objects in JSON format.
    """
    # File path for storing JSON data
    __file_path = "file.json"
    # Dictionary to hold objects
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects currently stored.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
        obj: The object to be added.
        """
        # Generate a unique key for the object and add it to the dictionary
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves the objects in the storage to a JSON file.
        """
        data = {}
        # Convert objects to dictionary format
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        # Write data to the JSON file
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Reloads the objects from the JSON file into the storage.
        """
        from models import (
            base_model,
            user,
            place,
            state,
            city,
            amenity,
            review
        )

        # Mapping of class names to corresponding modules
        module_mapping = {
            "BaseModel": base_model,
            "User": user,
            "Place": place,
            "State": state,
            "City": city,
            "Amenity": amenity,
            "Review": review
        }

        if os.path.exists(self.__file_path):
            # Read data from the JSON file
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                # Iterate through the data and create object instances
                for key, value in data.items():
                    class_name = value["__class__"]

                    if class_name in module_mapping:
                        model_module = module_mapping[class_name]
                        model_class = getattr(model_module, class_name)
                        obj_instance = model_class(**value)
                        self.__objects[key] = obj_instance
                    else:
                        print("Warning: Class " + class_name +
                              " not found in module mapping.")
