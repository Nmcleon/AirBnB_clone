#!/usr/bin/python3
"""
Test Place class
"""

from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
import unittest
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Testing database storage")
class TestPlace(unittest.TestCase):
    def test_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_save(self):
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_to_dict(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
