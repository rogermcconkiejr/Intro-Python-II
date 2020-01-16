# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room):
        self.room = room
        self.plItems = []

    def getItems(self, availableItems):
        itemInput = input("type which Item you'd like to take \n(leave empty if you don't want any):")
        for i in availableItems:
            if i == itemInput:
                self.plItems.append(itemInput)
                availableItems.remove(itemInput)

    def dropItems(self):
        itemInput = input("Any item you want to drop? (leave empty if no):")
        for i in self.plItems:
            if i == itemInput:
                self.plItems.remove(itemInput)



