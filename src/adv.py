from room import Room
from player import Player
# Declare all the 
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def displayIntro():
    print("")
    print("You awaken to find yourself at a crossroads.")
    print("")
    print("You can't remember how you got there")
    print("You can go North, South, East, or West.")
    print("")


displayIntro()

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",["rocks"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",["dusty-knife", "sword"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",["rocks","bird-eggs","hatchet"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",["dirt"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",["treasure","gold","rubies"]),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

curRoom = player.room
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# print(player.room) 

# path = input("Where will you go? (Choose N , S , E, W) or q to quit: ").upper()

# player.curRoom = player.
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(player.room)
availableItems = player.room.items
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
player.getItems(availableItems)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(f"Here's what you got:{player.plItems}")
player.dropItems()

game_status = True

while game_status:
    path = input('\nWhere do you want to go? (Input n, s, e, or w) or q to quit: \n')

    if path == 'q':
        print('See you next time!\n')
        game_status = False

    if path == 'n' or path == 'e' or path == 's' or path == 'w':
        attrib = f'{path}_to'

        if player.room.__dict__[attrib] == None:
                print('\nYou can not go that way! Please choose another direction.\n')

        else:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            player.room = player.room.__dict__[attrib]
            availableItems = player.room.items
            print(player.room)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            player.getItems(availableItems)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f"Here's what you got: {player.plItems}")
            player.dropItems()
            





# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.