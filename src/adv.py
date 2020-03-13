from src.room import Room
from src.player import Player
from src.item import Food, Egg, Sandwich, Rock

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. 
Alas, it is a dead end and you must go back South"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
    Sadly, it has already been completely emptied by earlier adventurers. 
    The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']

room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']


'''

***MAP***
                  <------> Narrow <----> Treasure Room!!!??? :(
                 |
                 V  
outside <----> Foyer <-----> Overlook(deadend)

'''

### ITEMS
rock = Rock()
sandwich = Sandwich()
egg = Egg()
bacon = Food("bacon", "This is wonderful", 200)

#
# Main
#

## Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name: "), room['outside'])
player.items.append(rock)
player.items.append(sandwich)
player.items.append(egg)
player.items.append(bacon)
print(player.current_room)
# Write a loop that:
#REPL
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
valid_directions = ("n", "s", "e", "w")
valid_inventory = str(player.items)
# print(valid_inventory)
while True:
    cmd = input("\nWhat direction will you go? (Press (q) to quit, (i) for inventory, to eat an item, enter item name~~~>) ")
    if cmd == "q":
        print(f"Farewell {player.name}, come back soon!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "i":
        player.print_inventory()
    elif cmd in valid_inventory:
        found_item = False
        for food in player.items:

            if food.name == cmd :
                player.eat(food)
                valid_inventory = str(player.items)
                found_item = True

    else:
        print("Please enter a valid Command")