# Class instantiation (Object construction)
# When the constructor is called:
    # A new instance of that clas is created
    # The _init_() method of the class is called w/ the new object as its first argument + additional in expression

class Product:
    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self.name = name
        self.price = price
        self.nutrition_info = nutrition_info
        self.inventory = 0

    # Define methods
    def increase_inventory(self, amount):
        self.inventory += amount

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def damage(self, amount):
        self.health -= amount
    def boost(self, amount):
        self.health += amount

>>> player = Player('<NAME>')
plumber = Player("Mario")

# Anything that calls an object can go on the left side of the method
lst = [plumber, "Mario"]
print(lst[0].health) # == 100

# A Class variable is an assignment inside the class that isn't inside a method body.
class Product:
    sales_tax = 0.07




