import random
from raichu import Raichu
class Pikachu:
    poketype = ['Electric']
    description = 'Pikachu is an Electric Type Pokemon. It evolves into Raichu.'
    pokemon = 'Pikachu'

    def __init__(self, name='Pikachu', level=1):
        self.stamina = 70 + random.randint(1, 15)
        self.attack = 124 + random.randint(1, 15)
        self.defense = 108 + random.randint(1, 15)
        self.cp = random.randint(10, level*25)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Spark', 'Thunder')
        elif moves == 2:
            self.moves = ('Spark', 'Brick Break')
        elif moves == 3:
            self.moves = ('Thunder Shock', 'Thunder')
        elif moves == 4:
            self.moves = ('Thunder Shock', 'Brick Break')
        elif moves == 5:
            self.moves = ('Quick Attack', 'Thunder')
        else:
            self.moves = ('Quick Attack', 'Brick Break')
#Generating size stats
        self.height = float(random.randint(100, 160))/100
        self.weight = float(random.randint(3000,6000))/100
    
    
    def evolve(self, lvl):
        return Raichu(self.name,self.cp, lvl)
