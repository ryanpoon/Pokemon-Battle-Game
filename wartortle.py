import random
from blastoise import Blastoise
class Wartortle:
    poketype = ['Water']
    description = "Its tail is large and covered with a rich, thick fur. The tail becomes increasingly deeper in color as Wartortle ages. The scratches on its shell are evidence of this Pokemon's toughness as a battler."
    pokemon = 'Wartortle'

    def __init__(self, name='Wartortle', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Squirtle':
            name = 'Wartortle'
        self.attack = 144 + random.randint(1, 15)
        self.defense = 176 + random.randint(1, 15)
        self.stamina = 118 + random.randint(1, 15)
        self.cp = int((random.randint(20, 30)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Bite', 'Aqua Jet')
        elif moves == 2:
            self.moves = ('Bite', 'Hydro Pump')
        elif moves == 3:
            self.moves = ('Bite', 'Ice Beam')
        elif moves == 4:
            self.moves = ('Water Gun', 'Aqua Jet')
        elif moves == 5:
            self.moves = ('Water Gun', 'Hydro Pump')
        else:
            self.moves = ('Water Gun', 'Ice Beam')
#Generating size stats
        self.height = float(random.randint(100, 160))/100
        self.weight = float(random.randint(4000,7500))/100
    
    
    def evolve(self, lvl):
        return Blastoise(self.name, self.cp, lvl)
