#!/usr/bin/python3
"""unittest for Review class"""

import uuid
import json
import unittest

from models import storage
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_review(unittest.TestCase):

    def test_user_review(self):
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_review_1(self):
        review = Review()
        review.place_id = "Mondstadt"
        self.assertEqual(review.place_id, "Mondstadt")
