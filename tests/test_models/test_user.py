#!/usr/bin/python3

import uuid
import json
from models.base_model import BaseModel
from models.user import User
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestUserAttributes(unittest.TestCase):
    """
    Test the User class attributes
    """
    def test_empty_email(self):
        user = User()
        self.assertEqual(user.email, "")

    def test_email(self):
        user = User()
        user.email = "monster@pacificpunch.com"
        self.assertEqual(user.email, "monster@pacificpunch.com")

    def test_empty_password(self):
        user = User()
        self.assertEqual(user.password, "")

    def test_password(self):
        user = User()
        user.password = "666"
        self.assertEqual(user.password, "666")

    def test_empty_first_name(self):
        user = User()
        self.assertEqual(user.first_name, "")

    def test_first_name(self):
        user = User()
        user.first_name = "Jason"
        self.assertEqual(user.first_name, "Jason")

    def test_last_name(self):
        user = User()
        user.last_name = "Statham"
        self.assertEqual(user.last_name, "Statham")

    def test_empty_last_name(self):
        user = User()
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
