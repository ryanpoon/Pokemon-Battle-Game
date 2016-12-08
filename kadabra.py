import random
from alakazam import Alakazam
class Kadabra:
    poketype = ['Psychic']
    description = "Kadabra emits a peculiar alpha wave if it develops a headache. Only those people with a particularly strong psyche can hope to become a trainer of this Pokemon."
    pokemon = 'Kadabra'
    def __init__(self, name='Kadabra', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*29)
        if name == 'Abra':
            name = 'Kadabra'
        self.attack = 232 + random.randint(1, 15)
        self.defense = 138 + random.randint(1, 15)
        self.stamina = 80 + random.randint(1, 15)
        self.cp = int((random.randint(13, 17)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Confusion', 'Dazzling Gleam')
        elif moves == 2:
            self.moves = ('Confusion', 'Psybeam')
        elif moves == 3:
            self.moves = ('Confusion', 'Shadow Ball')
        elif moves == 4:
            self.moves = ('Psycho Cut', 'Dazzling Gleam')
        elif moves == 5:
            self.moves = ('Psycho Cut', 'Psybeam')
        else:
            self.moves = ('Psycho Cut', 'Shadow Ball')
#Generating size stats
        self.height = float(random.randint(100, 160))/100
        self.weight = float(random.randint(4000,7500))/100
    
    
    def evolve(self, lvl):
        return Alakazam(self.name, self.cp, lvl)
