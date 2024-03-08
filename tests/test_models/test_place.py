#!/usr/bin/python3
""" unittests for place tests """

import uuid
import json
import unittest

from models import storage
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):

    def test_to_dict(self):
        place = Place()
        place_dict = place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], place.id)
        self.assertEqual(place_dict["created_at"],
                         place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"],
                         place.updated_at.isoformat())
        self.assertEqual(place_dict["name"], place.name)
        self.assertEqual(place_dict["city_id"], place.city_id)
        self.assertEqual(place_dict["user_id"], place.user_id)
        self.assertEqual(place_dict["description"], place.description)
        self.assertEqual(place_dict["number_rooms"], place.number_rooms)
        self.assertEqual(place_dict["number_bathrooms"],
                         place.number_bathrooms)
        self.assertEqual(place_dict["max_guest"], place.max_guest)
        self.assertEqual(place_dict["price_by_night"], place.price_by_night)
        self.assertEqual(place_dict["latitude"], place.latitude)
        self.assertEqual(place_dict["longitude"], place.longitude)
        self.assertEqual(place_dict["amenity_ids"], place.amenity_ids)

    def test_name(self):
        place = Place()
        place.name = "under the sea la la la la"
        self.assertEqual(place.city.id, "under the sea la la la la")

    def test_city_id(self):
        place = Place()
        place.city_id = "8.8.8.8"
        self.assertEqual(place.city_id, "8.8.8.8")
