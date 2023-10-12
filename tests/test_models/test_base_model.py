#!/usr/bin/python3

import unittest
import pep8
import models
from models.base_model import BaseModel
from datetime import datetime
import os



class TestBaseModel(unittest.TestCase):
	@classmethod
    def setUpClass(cls):
		cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

	def setUp(self):
		self.BM = BaseModel()
   
	def test_pep8_conformance_BaseModel(self):
		pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")
	
	def test_pep8_conformance_test_BaseModel(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")
	
	def test_module_docstring(self):
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
	
	def test_type(self):
        self.assertIsInstance(self.BM, BaseModel)
        self.assertEqual(type(self.BM), BaseModel)

	def test_basic_attribute_set(self):
        self.BM.first_name = 'Meco'
        self.BM.last_name = 'Montes'
        self.assertEqual(self.BM.first_name, 'Meco')
        self.assertEqual(self.BM.last_name, 'Montes')

    def test_str(self):
        string = str(self.BM)
        BMid = "[{}] ({}) {}".format(self.BM.__class__.__name__, self.BM.id, self.BM.__dict__)
        self.assertIn(BMid, string)
        self.assertIn("updated_at", string)
        self.assertIn("created_at", string)
        self.assertIn("datetime", string)

	def test_unique_id(self):
        BM1 = BaseModel()
        BM2 = BaseModel()
        self.assertNotEqual(self.BM.id, BM1.id)
        self.assertNotEqual(self.BM.id, BM2.id)

    def test_id_type_string(self):
        self.assertEqual(type(self.BM.id), str)

    def test_updated_time(self):
        time1 = self.BM.updated_at
        self.BM.save()
        time2 = self.BM.updated_at
        self.assertNotEqual(time1, time2)
        self.assertIsInstance(time1, datetime)

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

