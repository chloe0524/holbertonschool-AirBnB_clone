#!/usr/bin/python3

"""City module"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents a city within a specific state.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
