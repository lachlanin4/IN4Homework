class Room:
    """
    A Class that encapsulates the features of a room
    """

    def __init__(self, room_name):
        """
        Initialise member variables
        """
        self.room_name = room_name
        self.description = None
        self.linked_rooms = {}
        self._character = None

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, new_character):
        self._character = new_character

    @property
    def description(self):
        """
        Return a description of the room
        """
        return self._description

    @description.setter
    def description(self, room_description):
        """
        Set the description of the room
        """
        self._description = room_description

    def describe(self):
        """
        Print out a description of the room
        """
        print(self.description)

    @property
    def room_name(self):
        """
        Return the room name
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        """
        Set the room name
        """
        self._room_name = room_name

    def link_room(self, room_to_link, direction):
        """
        Link the room to another via a given direction
        """
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """
        Print out the details of the room
        """
        print(self.room_name)
        print("--------------------")
        print(self.description)
        """
    Iterate the dictionary and print out the connected rooms and directions.
    """
        for direction, room in self.linked_rooms.items():
            print(f"The {room.room_name} is {direction}")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
