#!/usr/bin/python3
"""
Test Review class
"""

from models import storage
from models.review import Review
from models.place import Place
from models.user import User
import unittest
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Testing database storage")
class TestReview(unittest.TestCase):
    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_save(self):
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
