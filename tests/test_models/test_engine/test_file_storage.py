#!/usr/bin/python3
"""Unit tests for FileStorage"""

import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Tests File Storage"""

    def test_path(self):
        """Test file_path"""
        file_storage = FileStorage()
        expected_file = 'file.json'
        self.assertEqual(file_storage._FileStorage__file_path, expected_file)

    def test_new(self):
        """Test new()"""
        file_storage = FileStorage()
        new_mod = BaseModel()
        file_storage.new(new_mod)
        self.assertIn("BaseModel." + new_mod.id,
                      file_storage._FileStorage__objects)

    def test_object(self):
        """Test _objects"""
        file_storage = FileStorage()
        self.assertIsInstance(file_storage._FileStorage__objects, dict)

    def test_all(self):
        """Test all()"""
        file_storage = FileStorage()
        new_dict = file_storage.all()
        self.assertIsInstance(new_dict, dict)
        self.assertIs(new_dict, file_storage._FileStorage__objects)

    def test_save(self):
        """Test save()"""
        file_storage = FileStorage()
        new_mod = BaseModel()
        file_storage.new(new_mod)
        file_storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + new_mod.id, json.load(f))

    def test_reload(self):
        """Test the reload of FileStorage class"""
        file_storage = FileStorage()
        new_mod = BaseModel()

        file_storage.new(new_mod)
        file_storage.save()
        file_storage.reload()

        with open("file.json", 'r') as file:
            self.assertIn("BaseModel." + new_mod.id, json.load(file))

        file_storage.save()
        file_storage._FileStorage__objects = {}
        file_storage.reload()
        self.assertNotEqual(file_storage.all(), {})


if __name__ == "__main__":
    unittest.main()
