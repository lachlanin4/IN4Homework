#!/usr/bin env python3

from character import Character
from enemy import Enemy

# Create character called dave
dave = Character("Dave", "A smelly zombie")

# Print out daves discription
dave.describe()

# Set daves conversation
dave.set_conversation("Hello I'm Dave and I'm new here")

# Make dave talk
dave.talk()

# Create Enemy named "bork"
bork = Enemy("bork", "A smelly zombie")

# Set a weakness
bork.set_weakness("cheese")

# Fight with dave
print("What will you fight with?")
fight_with = input()
bork.fight(fight_with)
