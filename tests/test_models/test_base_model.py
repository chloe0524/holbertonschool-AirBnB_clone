#!/usr/bin/python3
"""'unittests' for 'BaseModel class'"""

import uuid
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """'unittests' for BaseModel class"""

    def test_save(self):
        """Test save()"""
        new_mod = BaseModel()
        new_mod.save()
        self.assertNotEqual(new_mod.created_at, new_mod.updated_at)
        self.assertIsInstance(new_mod.updated_at, datetime.datetime)

    def test_created_at(self):
        """Test created_at"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test updated_at"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

    def test_id(self):
        """Test id"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_to_dict(self):
        """Test to_dict """
        new_mod = BaseModel()
        new_mod.name = "This is a model (to_dict test)"
        new_mod_json = new_mod.to_dict()
        self.assertEqual(new_mod_json["id"], new_mod.id)

    def test___str__(self):
        """Test __str__"""
        new_mod = BaseModel()
        new_mod.name = "This is a model (__str__ test)"
        self.assertEqual(str(new_mod),
                         "[BaseModel] ({}) {}".format
                         (new_mod.id, new_mod.__dict__))

    def test_init(self):
        """Test __init__()"""
        new_mod = BaseModel()
        self.assertIsInstance(new_mod, BaseModel)
        self.assertIsInstance(new_mod.id, str)
        self.assertIsInstance(new_mod.created_at, datetime.datetime)
        self.assertIsInstance(new_mod.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
