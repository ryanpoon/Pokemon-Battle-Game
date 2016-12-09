import random
from raichu import Raichu
class Pikachu:
    poketype = ['Electric']
    description = "Whenever Pikachu comes across something new, it blasts it with a jolt of electricity. If you come across a blackened berry, it's evidence that this Pokemon mistook the intensity of its charge."
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
            self.moves = ('Quick Attack', 'Discharge')
        elif moves == 2:
            self.moves = ('Thunder Shock', 'Thunder')
        elif moves == 3:
            self.moves = ('Thunder Shock', 'Thunderbolt')
        elif moves == 4:
            self.moves = ('Thunder Shock', 'Discharge')
        elif moves == 5:
            self.moves = ('Quick Attack', 'Thunder')
        else:
            self.moves = ('Quick Attack', 'Thunderbolt')
#Generating size stats
        self.height = float(random.randint(30, 50))/100
        self.weight = float(random.randint(500,700))/100
    
    
    def evolve(self, lvl):
        return Raichu(self.name,self.cp, lvl)
