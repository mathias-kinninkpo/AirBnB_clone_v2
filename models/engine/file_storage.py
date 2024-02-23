#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    __classes = {
            "User": User,
            "State": State,
            "City":  City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        cls = cls if not isinstance(cls, str) else self.__classes.get(cls)
        tmp = {}
        if cls:
            for key, value in FileStorage.__objects.items():
                if key.split(".")[0] == cls.__name__:
                    tmp[key] = value
            return tmp
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """to delete 'obj' from __objects"""
        if obj:
            key_obj = obj.to_dict()['__class__'] + '.' + obj.id
            FileStorage.__objects.pop(key_obj, None)

    def close(self):
        """Add a public method """
        self.reload()
