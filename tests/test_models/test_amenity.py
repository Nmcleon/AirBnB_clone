#!/usr/bin/python3
"""
Test Amenity class
"""

from models import storage
from models.amenity import Amenity
import unittest
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Testing database storage")
class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_save(self):
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
