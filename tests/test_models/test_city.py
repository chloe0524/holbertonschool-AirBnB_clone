#!/usr/bin/python3
"""
Module for City unittest
"""
import uuid
import json
from models.base_model import BaseModel
from models.city import City
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the State_id class attr
    """
    def test_user_city(self):
        city = City()
        self.assertEqual(city.state_id, "")

    def test_user_city_1(self):
        city = City()
        city.state_id = "France"
        self.assertEqual(city.state_id, "France")
