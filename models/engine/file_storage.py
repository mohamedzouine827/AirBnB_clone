#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        json_forma = {}
        for key in FileStorage.__objects.keys():
            json_forma[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_forma, f, indent=4)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r") as file:
                dictionary = json.load(file)
            for key, value in dictionary.items():
                class_name, id_class = key.split(".")
                if class_name in ["User", "Place", "City", "Amenity",
                                  "State", "Review"]:
                    clss = eval(class_name)(**value)
                else:
                    clss = eval(class_name)(**value)
                FileStorage.__objects[key] = clss
