#!/usr/bin/python3

"""Unittests for City class"""

import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
from models import storage


class TestCity(unittest.TestCase):

    def test_city_instance_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attr(self):
        city = City()
        city.state_id = "666"
        city.name = "Hell"

        self.assertEqual(city.state_id, "666")
        self.assertEqual(city.name, "Hell")


if __name__ == "__main__":
    unittest.main()