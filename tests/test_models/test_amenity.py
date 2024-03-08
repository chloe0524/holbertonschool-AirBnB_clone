#!/usr/bin/python3

import uuid
import json
import unittest

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class tests_amenity(unittest.TestCase):

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
