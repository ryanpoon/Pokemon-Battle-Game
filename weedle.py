import random
from kakuna import Kakuna
class Weedle:
    poketype = ['Poison','Bug']
    description = 'Weedle is a small larva Pokemon with a segmented body ranging in color from yellow to reddish-brown.'
    pokemon = 'Weedle'

    def __init__(self, name='Weedle', level=1):
        self.stamina = 80 + random.randint(1, 15)
        self.attack = 68 + random.randint(1, 15)
        self.defense = 64 + random.randint(1, 15)
        self.cp = random.randint(10, level*15)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,3)
        if moves == 1:
            self.moves = ('Poison Sting', 'Struggle')
        else:
            self.moves = ('Bug Bite', 'Struggle')
        
        
#Generating size stats
        self.height = float(random.randint(100, 160))/1000
        self.weight = float(random.randint(3000,6000))/10000
    
    
    def evolve(self, lvl):
        return Kakuna(self.name, self.cp, lvl)
        
