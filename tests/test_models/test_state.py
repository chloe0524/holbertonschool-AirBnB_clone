#!/usr/bin/python3
"""
Module for City unittest
"""
import uuid
import json
from models.base_model import BaseModel
from models.state import State
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the State_id class attr
    """
    def test_user_state(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_user_city_1(self):
        state = State()
        state.name = "France"
        self.assertEqual(state.name, "France")
