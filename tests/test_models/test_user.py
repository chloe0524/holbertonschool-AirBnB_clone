#!/usr/bin/python3

import uuid
import json
import unittest

from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):

    def test_email(self):
        self.user.email = "monster@pacificpunch.com"
        self.assertEqual(self.user.email, "monster@pacificpunch.com")

    def test_password(self):
        self.user.password = "multilevelBAD123"
        self.assertEqual(self.user.password, "multilevelBAD123")

    def test_empty_email(self):
        with self.assertRaises(ValueError):
            self.user.email = ""

    def test_empty_password(self):
        with self.assertRaises(ValueError):
            self.user.password = ""


if __name__ == '__main__':
    unittest.main()
