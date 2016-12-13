import random
from kakuna import Kakuna
class Weedle:
    poketype = ['Poison','Bug']
    description = "Weedle has an extremely acute sense of smell. It is capable of distinguishing its favorite kinds of leaves from those it dislikes just by sniffing with its big red proboscis (nose)."
    pokemon = 'Weedle'

    def __init__(self, name='Weedle', level=1):
        self.stamina = 80 + random.randint(1, 15)
        self.attack = 63 + random.randint(1, 15)
        self.defense = 55 + random.randint(1, 15)
        self.cp = random.randint(10, level*10)
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
        self.height = float(random.randint(20, 40))/1000
        self.weight = float(random.randint(200,400))/10000
    
    
    def evolve(self, lvl):
        return Kakuna(self.name, self.cp, lvl)
        
