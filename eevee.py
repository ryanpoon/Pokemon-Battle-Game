import random
from jolteon import Jolteon
from vaporeon import Vaporeon
from flareon import Flareon
class Eevee:
    poketype = ['Normal']
    description = 'Eevee has an unstable genetic makeup that suddenly mutates due to the environment in which it lives. Radiation from various stones causes this Pokemon to evolve.'
    pokemon = 'Eevee'

    def __init__(self, name='Eevee', level=1):
        self.stamina = 110 + random.randint(1, 15)
        self.attack = 114 + random.randint(1, 15)
        self.defense = 128 + random.randint(1, 15)
        self.cp = random.randint(10, level*25)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Quick Attack', 'Body Slam')
        elif moves == 2:
            self.moves = ('Quick Attack', 'Dig')
        elif moves == 3:
            self.moves = ('Quick Attack', 'Swift')
        elif moves == 4:
            self.moves = ('Tackle', 'Body Slam')
        elif moves == 5:
            self.moves = ('Tackle', 'Dig')
        else:
            self.moves = ('Tackle', 'Swift')
#Generating size stats
        self.height = float(random.randint(15, 45))/100
        self.weight = float(random.randint(300,900))/100
    
    def evolve(self, lvl):
        eevolution = random.randint(1, 4)
        if eevolution == 1:
            return Flareon(self.name, self.cp, lvl)
        elif eevolution == 2:
            return Vaporeon(self.name, self.cp, lvl)
        return Jolteon(self.name,self.cp, lvl)
