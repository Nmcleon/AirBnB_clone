#!/usr/bin/python3
"""
Test City class
"""

from models import storage
from models.city import City
from models.state import State
import unittest
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') ==
                 'db', "Testing database storage")
class TestCity(unittest.TestCase):
    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_save(self):
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
