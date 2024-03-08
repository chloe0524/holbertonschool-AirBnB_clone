#!/usr/bin/python3
""" unittests for amenity class """

import uuid
import json
import unittest

from models import storage
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class tests_amenity(unittest.TestCase):
    """ Test amenity class"""

    def test_user_amenity(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_user_city_1(self):
        amenity = Amenity()
        amenity.name = "France"
        self.assertEqual(amenity.name, "France")
