import random
from beedrill import Beedrill
class Kakuna:
    poketype = ['Bug', 'Poison']
    description = 'Kakuna remains virtually immobile as it clings to a tree. However, on the inside, it is extremely busy as it prepares for its coming evolution. This is evident from how hot the shell becomes to the touch.'
    pokemon = 'Kakuna'

    def __init__(self, name='Kakuna', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10, level*10)
        if name == 'Weedle':
            name = 'Kakuna'
        self.attack = 46 + random.randint(1, 15)
        self.defense = 86 + random.randint(1, 15)
        self.cp = startcp
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,3)
        if moves == 1:
            self.moves = ('Bug Bite', 'Struggle')
        else:
            self.moves = ('Poison Sting', 'Struggle')
 
#Generating size stats
        self.height = float(random.randint(45, 75))/100
        self.weight = float(random.randint(500,1500))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Beedrill(self.name, self.cp)
    
