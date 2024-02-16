#!/usr/bin/python3
''' class User that inherits from BaseModel '''

from models.base_model import BaseModel


class User(BaseModel):
    ''' Atributos de clase pública '''
    # Attribute for User
    email = ""
    password = ""
    first_name = ""
    last_name = ""
