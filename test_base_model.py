#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = State()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.region = "NY"
my_user.home_town = "El Pablo"
my_user.save()
print(my_user)
