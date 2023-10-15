#!/usr/bin/python3
"""
test the functionality of file_storage.py
"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorageSave(unittest.TestCase):
    def setUp(self):
        self.fs = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = User()

    def test_save(self):
        """Test the save method"""
        self.fs.new(self.obj1)
        self.fs.new(self.obj2)
        self.fs.save()

        with open("file.jason", "r") as file:
            data = json.load(file)

        key1 = "{}.{}".format(self.obj1.__class__.__name__, self.obj.id)
        key2 = "{}.{}".format(self.obj2.__class__.__name__, self.obj2.id)

        self.assertTrue(key1 in data)
        self.assertTrue(key2 in data)

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

class TestFileStorageReload(unittest.TestCase):
    def setUp(self):
        self.fs = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = User()

    def test_reload(self):
        """Test reload method"""
        with open("file.jason", "w") as file:
            data = {
                    "{}.{}".format(self.obj1.__class__.__name__, self.obj1.id): self.obj1.to_dict(),
                    "{}.{}".format(self.obj2.__class__.__name__, self.obj2.id): self.obj2.to_dict()
                    }
            json.dump(data, file)

        self.fs.reload()
        all_objects = self.fs.all()

        key1 = "{}.{}".format(self.obj1.__class__.__name__, self.obj1.id)
        key2 = "{}.{}".format(self.obj2.__class__.__name__, self.obj2.id)

        self.assertTrue(key1 in all_objects)
        self.assertTrue(key2 in all_objects)

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
