#!/usr/bin/python3
"""Module for Base Model unittests."""
import uuid
import unittest
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests Base Model class."""
    def test_save(self):
        """Test save()"""
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_save2(self):
        my_model = BaseModel()
        my_model.save()
        expected = "BaseModel." + my_model.id
        with open("file.json", "r") as f:
            self.assertIn(expected, f.read())

    def test_to_dict(self):
        """Test to_dict()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["created_at"],
                         my_model.created_at.isoformat())

    def test__str__(self):
        """Test __str__()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.number = 89
        self.assertEqual(str(my_model),
                         f"[BaseModel] ({my_model.id}) {my_model.__dict__}")

    def test_init(self):
        """Test __init__()"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
