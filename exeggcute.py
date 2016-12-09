import random
from exeggutor import Exeggutor
class Exeggcute:
    poketype = ['Grass', 'Psychic']
    description = "This Pokemon consists of six eggs that form a closely knit cluster. The six eggs attract each other and spin around. When cracks increasingly appear on the eggs, Exeggcute is close to evolution."
    pokemon = 'Exeggcute'

    def __init__(self, name='Exeggcute', level=1):
        self.stamina = 120 + random.randint(1, 15)
        self.attack = 107 + random.randint(1, 15)
        self.defense = 140 + random.randint(1, 15)
        self.cp = random.randint(10, level*23)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,4)
        if moves == 1:
            self.moves = ('Confusion', 'Ancient Power')
        elif moves == 2:
            self.moves = ('Confusion', 'Psychic')
        else:
            self.moves = ('Confusion', 'Seed Bomb')
#Generating size stats
        self.height = float(random.randint(20, 60))/100
        self.weight = float(random.randint(200,300))/100
    
    
    def evolve(self, lvl):
        return Exeggutor(self.name,self.cp, lvl)
