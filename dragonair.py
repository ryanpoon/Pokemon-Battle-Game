import random
from dragonite import Dragonite
class Dragonair:
    poketype = ['Dragon']
    description = "Dragonair stores an enormous amount of energy inside its body. It is said to alter weather conditions in its vicinity by discharging energy from its crystals on its neck and tail."
    pokemon = 'Dragonair'

    def __init__(self, name='Dragonair', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10, level*21)
        if name == 'Dratini':
            name = 'Dragonair'
        self.attack = 163 + random.randint(1, 15)
        self.defense = 138 + random.randint(1, 15)
        self.cp = int((random.randint(15, 25)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,4)
        if moves == 1:
            self.moves = ('Dragon Breath', 'Aqua Tail')
        elif moves == 2:
            self.moves = ('Dragon Breath', 'Dragon Pulse')
        else:
            self.moves = ('Dragon Breath', 'Wrap')
    
#Generating size stats
        self.height = float(random.randint(300, 500))/100
        self.weight = float(random.randint(1300,1900))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Dragonite(self.name, self.cp, lvl)
