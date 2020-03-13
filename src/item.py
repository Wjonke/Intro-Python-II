class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return self.name

class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories


class Egg(Food):
    def __init__(self):
        super().__init__("egg", "This is an egg", 20)

class Rock(Food):
    def __init__(self):
        super().__init__("rock", "This is rock, why are you eating a rock", 1)

class Sandwich(Food):
    def __init__(self):
        super().__init__("sandwich", "This is a sandwich", 100)