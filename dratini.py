import random
from dragonair import Dragonair
class Dratini:
    poketype = ['Dragon']
    description = 'Dratini continually molts and sloughs off its old skin. It does so because the life energy within its body steadily builds to reach uncontrollable levels.'
    pokemon = 'Dratini'

    def __init__(self, name='Dratini', level=1):
        self.attack = 119 + random.randint(1, 15)
        self.defense = 94 + random.randint(1, 15)
        self.cp = random.randint(10, level*21)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Bite', 'Aqua Tail')
        elif moves == 2:
            self.moves = ('Bite', 'Wrap')
        elif moves == 3:
            self.moves = ('Bite', 'Twister')
        elif moves ==4:
            self.moves = ('Dragon Breath', 'Aqua Tail')
        elif moves == 5:
            self.moves = ('Dragon Breath', 'Wrap')
        else:
            self.moves = ('Dragon Breath', 'Twister')
#Generating size stats
        self.height = float(random.randint(150, 210))/100
        self.weight = float(random.randint(150,450))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Dragonair(self.name, self.cp, lvl)
