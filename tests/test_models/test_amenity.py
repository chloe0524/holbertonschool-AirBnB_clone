#!/usr/bin/python3

import uuid
import json
import unittest

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class tests_amenity(unittest.TestCase):

    def test_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["id"], amenity.id)
        self.assertEqual(amenity_dict["created_at"],
                         amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"],
                         amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict["name"], amenity.name)

    def test_name(self):
        """Test name attribute"""
        amenity = Amenity()
        amenity.name = "Rainbow"

        self.assertEqual(amenity.name, "Rainbow")

    def test_id(self):
        """Test if id attribute"""
        amenity = Amenity()
        amenity.id = "1234"

        self.assertEqual(amenity.id, "1234")
