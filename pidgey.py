import random
from pidgeotto import Pidgeotto
class Pidgey:
    poketype = ['Flying', 'Normal']
    description = 'Pidgey is a small, plump-bodied avian Pokemon. It is primarily brown with a cream colored face, underside, and flight feathers.'
    pokemon = 'Pidgey'

    def __init__(self, name='Pidgey', level=1):
        self.attack = 94 + random.randint(1, 15)
        self.defense = 90 + random.randint(1, 15)
        self.cp = random.randint(10, level*15)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,5)
        if moves == 1:
            self.moves = ('Fly', 'Gust')
        elif moves == 2:
            self.moves = ('Fly', 'Twister')
        elif moves == 3:
            self.moves = ('Quick Attack', 'Gust')
        else:
            self.moves = ('Quick Attack', 'Twister')
#Generating size stats
        self.height = float(random.randint(30, 60))/100
        self.weight = float(random.randint(600,1000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Pidgeotto(self.name, self.cp, lvl)
