#!/usr/bin/python3
""" All those classes that inherit from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    state_id = ""
    name = ""
