#!/usr/bin/python3
""" unittests for state class """

import uuid
import json
import unittest

from models import storage
from models.state import State
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_state(unittest.TestCase):

    def test_to_dict(self):
        state = State()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["id"], state.id)
        self.assertEqual(state_dict["created_at"],
                         state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"],
                         state.updated_at.isoformat())
        self.assertEqual(state_dict["name"], state.name)

    def test_name(self):
        state = State()
        state.name = "Ohio"
        self.assertEqual(state.name, "Ohio")

    def test_name_empty(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_of_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)
