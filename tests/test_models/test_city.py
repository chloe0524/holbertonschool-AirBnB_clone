#!/usr/bin/python3

"""Unittests for City class."""

import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
from models import storage


class TestCity(unittest.TestCase):


    def test_city_instance_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

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
        city.state_id = "666"
        self.assertEqual(city.state_id, "666")


if __name__ == "__main__":
    unittest.main()
