#!/usr/bin/python3

import uuid
import json
import unittest

from models import storage
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):

    def test_to_dict(self):
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["id"], city.id)
        self.assertEqual(city_dict["created_at"],
                         city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"],
                         city.updated_at.isoformat())
        self.assertEqual(city_dict["name"], city.name)
        self.assertEqual(city_dict["state_id"], city.state_id)

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
