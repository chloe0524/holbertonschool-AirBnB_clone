#!/usr/bin/python3

"""unittests for State class"""

import uuid
import json
import unittest

from models import storage
from models.state import State
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_state(unittest.TestCase):


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
