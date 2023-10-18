#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ class for serializing and deserializing    """
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """init file storage"""
        pass

    def all(self):
        """returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        dictionary = obj.to_dict()
        key = '{}.{}'.format(dictionary['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the file.json"""
        dictionary = dict()
        for i, j in FileStorage.__objects.items():
            dictionary[i] = j.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        """deserialize file.json"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for i, j in json_load.items():
                FileStorage.__objects[i] = BaseModel(**j)
        except:
            pass
