#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class FileStorage:
    __file_path = os.path.abspath(os.path.dirname(__file__) + "/file.json")
    __objects = {}
    classes = {}

    def __init__(self):
        """init file storage"""
        self.classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_data = {}
        for key, value in FileStorage.__objects.items():
            serialized_data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        with open(FileStorage.__file_path, 'r') as file:
            serialized_data = json.load(file)
        for key, value in serialized_data.items():
            class_name, obj_id = key.split(".")
            if class_name in self.classes:
                obj = self.classes[class_name]()
                obj.id = obj_id
                for attr, val in value.items():
                    if attr in obj.__dict__:
                        obj.__dict__[attr] = val
                FileStorage.__objects[key] = obj

    def _serialize_user(self, obj):
        if isinstance(obj, User):
            return {
                    "__class__": "User",
                    "id": obj.id,
                    "email": obj.email,
                    "password": obj.password,
                    "first_name": obj.first_name,
                    "last_name": obj.last_name,
                    "created_at": obj.created_at.isoformat(),
                    "updated_at": obj.updated_at.isoformat(),
                    }
        else:
            raise TypeError("Type not serializable")

    def _deserialize_user(self, data):
        if data["__class__"] == "User":
            user = User()
            user.id = data["id"]
            user.email = data["email"]
            user.password = data["password"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.created_at = datetime.fromisoformat(data["created_at"])
            user.updated_at = datetime.fromisoformat(data["updated_at"])
            return user
        else:
            raise TypeError("Type not deserializable")
