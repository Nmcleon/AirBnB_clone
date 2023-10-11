#!/usr/bin/python3
"""
base model
"""

import uuid
from datetime import datetime

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
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Update 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary representation of BaseModel instance.
        Includes 'id', 'created_at', 'updated_at', and '__class__' keys.
        'created_at' and 'updated_at' are converted to ISO format.
        """
        class_name = self.__class__.__name__
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": class_name,
        }

    def __str__(self):
        """
        Returns string representation of BaseModel instance.
        - Includes the class name, 'id', and the instance's dictionary representation.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
