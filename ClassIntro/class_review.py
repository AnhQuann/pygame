# data abstraction
# java, c# = closed
# python = open
from random import choice, randint

class Food:
    #x, y, name, hp_buff
    def __init__(self, x, y, name, hp_buff):
        self.x = x
        self.y = y
        self.name = name
        self.hp_buff = hp_buff

    def print(self):
        print("{{ {0}, {1}, {2}, {3} }}".format(self.x, self.y, self.name, self.hp_buff))

list_item = []

for i in range(10):
    x = randint(0,10)
    y = randint(0,10)
    name = choice(["HP, Mana, Strength, Agi, Intel"])
    hp_buff = randint(0, 100)

    food = Food(x, y, name, hp_buff)
    list_item.append(food)
    

# food1 = Food(0, 0, "HP", 100) # objects, construct a objects
# food1.print()
