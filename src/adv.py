from room import Room
from player import Player
# Declare all the 

# def displayIntro():
#     print("You awaken to find yourself at a crossroads.")
#     print("You can't remember how you got there")
#     print("You can go North, South, East, or West.")


# def choosePath():
#     path = ""
#     while path != "N" and path != "S" and path != "E" and path != "W":
#         input("Which path do you choose? (input N , S , E, or W): ").upper()
#         return path

# displayIntro()
# choosePath()

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
print(player.room) 

path = input("Where will you go? (Choose N , S , E, W) or q to quit: ").upper()

player.curRoom = player.room

def outsidePath(path,func1):
    while path != "Q":
        if path == "N":
            player = Player(room['foyer'])
            print(player.room)
            func1(path)
            break
        elif path == "S" or "E" or "W":
            print("You can not go that way . . .")
            path = input("Where will you go? (Choose N , S , E, W): ").upper()
        else:
            print("Please enter a valid direction!")

def foyerPath(func1):
    path = input("Where will you go? (Choose N , S , E, W) or q to quit: ").upper()
    while path != "Q":
        if path == "S":
            player = Player(room['outside'])
            print(player.room)
            func1(path)
            break
        elif path == "N":
            player = Player(room['overlook'])
            print(player.room)
            break
        elif path == "E":
            player = Player(room['narrow'])
            print(player.room)
            break
        elif path == "W":
            print("You can not go that way . . .")
            path = input("Where will you go? (Choose N , S , E, W): ").upper()        
        else:
            print("Please enter a valid direction!")
outsidePath(path, foyerPath)
foyerPath(outsidePath)


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
