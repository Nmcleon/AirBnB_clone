#!/usr/bin/python3
"""
base model
"""

import json
import os
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        This method initializes a BaseModel instance.
        Sets a unique 'id' for the instance.
        Sets 'created_at' and 'updated_at' attributes to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of BaseModel instance.
        - Includes the class name, 'id', and the instance's dictionary representation.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary representation of BaseModel instance.
        Includes 'id', 'created_at', 'updated_at', and '__class__' keys.
        'created_at' and 'updated_at' are converted to ISO format.
        """
        data = self.__dict__.copy()
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        data["__class__"] = self.__class__.__name__      
        return data
