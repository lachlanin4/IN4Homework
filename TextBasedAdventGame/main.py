from enemy import Enemy
from room import Room

kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
kitchen.describe()
ballroom = Room("ballroom")
ballroom.description = "A room full of balls"
dining_hall = Room("dining hall")
dining_hall.description = "A room with a long table, one chair and a distinct smell"

# Add enemy dave to proceedings
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh.. rgrhl... brains...")
dave.set_weakness("cheese")

kitchen.link_room(dining_hall, "South")
dining_hall.link_room(kitchen, "North")
dining_hall.link_room(ballroom, "West")
ballroom.link_room(dining_hall, "East")

dining_hall.character = dave

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)
