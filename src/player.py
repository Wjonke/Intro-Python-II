# Write a class to hold player information, e.g. what room they are in
from src.item import Food
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.strength = 100

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("You cannot move in that direction, unless you can walk through walls..")

    def print_inventory(self):
        print("You are holding the following items in inventory: ")
        for item in self.items:
            print("~~>", item.name)

    def eat(self, food_item):
        if not isinstance(food_item, Food):
            print(f"You dont have {food_item.name}")
        else:
            self.strength += food_item.calories
            print(f"You have eaten {food_item.name}, your strength is now {self.strength}")
            self.items.remove(food_item)
            