#!/usr/bin/python3
"""Defines City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent A City
    Attributes:
            name (str): Name of the city
            state_id (str): state id
    """

    state_id = ""
    name = ""
