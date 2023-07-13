#!/usr/bin env python3

from character import Character
from enemy import Enemy

dave = Character("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Hello I'm Dave and I'm new here")
dave.talk()

bork = Enemy("bork", "A smelly zombie")
