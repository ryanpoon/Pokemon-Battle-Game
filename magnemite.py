import random
from magneton import Magneton
class Magnemite:
    poketype = ['Electric', 'Steel']
    description = "Magnemite attaches itself to power lines to feed on electricity. If your house has a power outage, check your circuit breakers. You may find a large number of this Pokemon clinging to the breaker box."
    pokemon = 'Magnemite'

    def __init__(self, name='Magnemite', level=1):
        self.attack = 165 + random.randint(1, 15)
        self.defense = 128 + random.randint(1, 15)
        self.cp = random.randint(10, level*27)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Spark', 'Discharge')
        elif moves == 2:
            self.moves = ('Spark', 'Magnet Bomb')
        elif moves == 3:
            self.moves = ('Spark', 'Thunderbolt')
        elif moves == 4:
            self.moves = ('Thunder Shock', 'Discharge')
        elif moves == 5:
            self.moves = ('Thunder Shock', 'Magnet Bomb')
        else:
            self.moves = ('Thunder Shock', 'Thunderbolt')
#Generating size stats
        self.height = float(random.randint(20, 40))/100
        self.weight = float(random.randint(400, 800))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Magneton(self.name, self.cp, lvl)
