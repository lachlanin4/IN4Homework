#!/usr/bin env python3
from character import Character

class Enemy(Character):
    """
    A Class that encapsulates the features of a enemy
    """

    # Create a character
    def __init__(self, char_name, char_description):
       super().__init__(char_name, char_description)
