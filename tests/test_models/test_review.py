#!/usr/bin/python3
""" unittests for review class """

import uuid
import json
import unittest

from models import storage
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_review(unittest.TestCase):

    def test_to_dict(self):
        review = Review()
        review_dict = review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["id"], review.id)
        self.assertEqual(review_dict["created_at"],
                         review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"],
                         review.updated_at.isoformat())
        self.assertEqual(review_dict["text"], review.text)
        self.assertEqual(review_dict["user_id"], review.user_id)
        self.assertEqual(review_dict["place_id"], review.place_id)

    def test_text(self):
        review = Review()
        review.text = "owlbear cub sumpremacy"
        self.assertEqual(review.text, "owlbear cub sumpremacy")

    def test_user_id(self):
        review = Review()
        review.user_id = "5652"
        self.assertEqual(review.user_id, "5652")
