import random
from pidgeot import Pidgeot
class Pidgeotto:
    poketype = ['Normal', 'Flying']
    description = 'Pidgeotto claims a large area as its own territory. This Pokemon flies around, patrolling its living space. If its territory is violated, it shows no mercy in thoroughly punishing the foe with its sharp claws.'
    pokemon = 'Pidgeotto'

    def __init__(self, name='Pidgeotto', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10, level*15)
        if name == 'Pidgey':
            name = 'Pidgeotto'
        self.attack = 117 + random.randint(1, 15)
        self.defense = 108 + random.randint(1, 15)
        self.cp = int((random.randint(17, 19)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,5)
        if moves == 1:
            self.moves = ('Steel Wing', 'Aerial Ace')
        elif moves == 2:
            self.moves = ('Steel Wing', 'Twister')
        elif moves == 3:
            self.moves = ('Steel Wing', 'Air Cutter')
        elif moves == 4:
            self.moves = ('Wing Attack', 'Aerial Ace')
        elif moves == 5:
            self.moves = ('Wing Attack', 'Air Cutter')
        else:
            self.moves = ('Wing Attack', 'Twister')
#Generating size stats
        self.height = float(random.randint(80, 120))/100
        self.weight = float(random.randint(2000,4000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Pidgeot(self.name, self.cp, lvl)
