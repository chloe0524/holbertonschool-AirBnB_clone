#!/usr/bin/python3
"""
Module for Review unittest
"""
import uuid
import json
from models.base_model import BaseModel
from models.review import Review
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the State_id class attr
    """
    def test_user_review(self):
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_review_1(self):
        review = Review()
        review.place_id = "Paris"
        self.assertEqual(review.place_id, "Paris")
