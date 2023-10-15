#!/usr/bin/python3

import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel
from models.engine import file_storage


class TestUser(unittest.TestCase):
    def test_pep8(self):
        """Check PEP8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors")

    def test_user_instance(self):
        """Check if user is instance of User"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Check if User instance has listed attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_attributes_type(self):
        """Check data types of User attributes"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == "__main__":
    unittest.main()
