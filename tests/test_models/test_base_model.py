#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    def test_instance_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_save_method(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertEqual(
            my_model_json["created_at"],
            my_model.created_at.isoformat()
        )
        self.assertEqual(
            my_model_json["updated_at"],
            my_model.updated_at.isoformat()
        )

    def test_str_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        str_repr = str(my_model)
        self.assertIn("[BaseModel] ({})".format(my_model.id), str_repr)
        self.assertIn("'name': 'My First Model'", str_repr)
        self.assertIn("'my_number': 89", str_repr)
        self.assertIn("'__class__': 'BaseModel'", str_repr)

if __name__ == "__main__":
    unittest.main()
