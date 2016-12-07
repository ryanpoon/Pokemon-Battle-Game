import random
from charizard import Charizard
class Charmeleon:
    poketype = ['Fire']
    description = "Charmeleon mercilessly destroys its foes using its sharp claws. If it encounters a strong foe, it turns aggressive. In this excited state, the flame at the tip of its tail flares with a bluish white color."
    pokemon = 'Charmeleon'

    def __init__(self, name='Charmeleon', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Charmander':
            name = 'Charmeleon'
        self.attack = 160 + random.randint(1, 15)
        self.defense = 140 + random.randint(1, 15)
        self.stamina = 116 + random.randint(1, 15)
        self.cp = int((random.randint(20, 30)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Ember', 'Flame Burst')
        elif moves == 2:
            self.moves = ('Ember', 'Fire Punch')
        elif moves == 3:
            self.moves = ('Ember', 'Flamethrower')
        elif moves == 4:
            self.moves = ('Scratch', 'Flame Burst')
        elif moves == 5:
            self.moves = ('Scratch', 'Fire Punch')
        else:
            self.moves = ('Scratch', 'Flamethrower')
#Generating size stats
        self.height = float(random.randint(70, 130))/100
        self.weight = float(random.randint(1700,2100))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Charizard(self.name, self.cp, lvl)
