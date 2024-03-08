#!/usr/bin/python3
"""
Module for Amenity unittest
"""
import uuid
import json
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the State_id class attr
    """
    def test_user_amenity(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_user_city_1(self):
        amenity = Amenity()
        amenity.name = "France"
        self.assertEqual(amenity.name, "France")
