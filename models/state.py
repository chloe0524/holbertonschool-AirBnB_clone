#!/usr/bin/python3

"""State module """
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class represents a specific state or province.

    Attributes:
        name (str): The name of the state.
    """
    name = ""