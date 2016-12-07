import random
from gengar import Gengar
class Haunter:
    poketype = ['Ghost', 'Poison']
    description = "Haunter is a dangerous Pokémon. If one beckons you while floating in darkness, you must never approach it. This Pokemon will try to lick you with its tongue and steal your life away."
    pokemon = 'Haunter'

    def __init__(self, name='Haunter', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Gastly':
            name = 'Haunter'
        self.attack = 90 + random.randint(1, 15)
        self.defense = 223 + random.randint(1, 15)
        self.stamina = 112 + random.randint(1, 15)
        self.cp = int((random.randint(13, 21)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Lick', 'Dark Pulse')
        elif moves == 2:
            self.moves = ('Lick', 'Shadow Ball')
        elif moves == 3:
            self.moves = ('Lick', 'Sludge Bomb')
        elif moves == 4:
            self.moves = ('Shadow Claw', 'Dark Pulse')
        elif moves == 5:
            self.moves = ('Shadow Claw', 'Shadow Ball')
        else:
            self.moves = ('Shadow Claw', 'Sludge Bomb')
#Generating size stats
        self.height = float(random.randint(100, 190))/100
        self.weight = float(random.randint(9,11))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Gengar(self.name, self.cp, lvl)
