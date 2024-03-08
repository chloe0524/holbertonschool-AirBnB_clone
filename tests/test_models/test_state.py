#!/usr/bin/python3
""" unittests for state class """

import uuid
import json
import unittest

from models import storage
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_state(unittest.TestCase):

    def test_name(self):
        state = State()
        state.name = "Ohio"
        self.assertEqual(state.name, "Ohio")
