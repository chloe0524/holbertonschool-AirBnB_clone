#!/usr/bin/python3
""" unittests for place tests """

import uuid
import json
import unittest

from models import storage
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):

    def test_name(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_city_id(self):
        place = Place()
        place.city_id = "8.8.8.8"
        self.assertEqual(place.city_id, "8.8.8.8")
