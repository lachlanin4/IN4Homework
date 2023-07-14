#!/usr/bin env python3
from character import Character

class Enemy(Character):
    """
    A Class that encapsulates the features of a enemy
    """

    # Create a character
    def __init__(self, char_name, char_description, weakness=None):
       super().__init__(char_name, char_description)
       self._weakness = weakness

    @property
    def weakness(self):
       return self._weakness

    @weakness.setter
    def weakness(self, item_weakness):
        self._item_weakness = item_weakness

    def set_weakness(self, item_weakness):
       self._weakness = item_weakness

    def fight(self, combat_item):
       if combat_item == self.weakness:
          print("You fend " + self.name + " off with the " + combat_item)
          return True
      else:
          print(self.name + " crushes you, puny adventurer")
          return False
