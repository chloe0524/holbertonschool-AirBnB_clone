#!/usr/bin/python3
""" unittests for city class """
import uuid
import json
import unittest

from models import storage
from models.city import City
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):


    def test_name(self):
        city = City()
        city.name = (
            "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
        )
        self.assertEqual(
            city.name,
            "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
        )

    def test_state_id(self):
        city = City()
        city.state_id = "1234"
        self.assertEqual(city.state_id, "1234")
