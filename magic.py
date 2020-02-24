import random

class Spell:
    def __init__(self, name, cost, dmg, type1):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type1 = type1

    def gen_dmg(self):
        low = self.dmg-15
        high = self.dmg+15
        return random.randrange(low, high)
