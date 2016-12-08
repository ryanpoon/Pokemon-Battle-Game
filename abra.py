import random
from kadabra import Kadabra
class Abra:
    poketype = ['Psychic']
    description = "Abra sleeps for eighteen hours a day. However, it can sense the presence of foes even while it is sleeping. In such a situation, this Pokemon immediately teleports to safety."
    pokemon = 'Abra'

    def __init__(self, name='Abra', level=1):
        self.attack = 195 + random.randint(1, 15)
        self.defense = 103 + random.randint(1, 15)
        self.stamina = 50 + random.randint(1, 15)
        self.cp = random.randint(10, level*29)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,4)
        if moves == 1:
            self.moves = ('Zen Headbutt', 'Psyshock')
        elif moves == 2:
            self.moves = ('Zen Headbutt', 'Shadow Ball')
        else:
            self.moves = ('Zen Headbutt', 'Signal Beam')
#Generating size stats
        self.height = float(random.randint(700, 1100))/100
        self.weight = float(random.randint(1700, 2100))/100
    
    def evolve(self, lvl):
        return Kadabra(self.name,self.cp, lvl)
