#!/usr/bin/python3
"""
Test State class
"""

from models import storage
from models.state import State
import unittest
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') ==
                 'db', "Testing database storage")
class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_save(self):
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict(self):
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
