import random
from wartortle import Wartortle
class Squirtle:
    poketype = ['Water']
    description = "Squirtle's shell is not merely used for protection. The shell's rounded shape and the grooves on its surface help minimize resistance in water, enabling this Pokemon to swim at high speeds."
    pokemon = 'Squirtle'

    def __init__(self, name='Squirtle', level=1):
        self.attack = 112 + random.randint(1, 15)
        self.defense = 142 + random.randint(1, 15)
        self.stamina = 88 + random.randint(1, 15)
        self.cp = random.randint(10, level*25)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Bubble', 'Aqua Jet')
        elif moves == 2:
            self.moves = ('Bubble', 'Aqua Tail')
        elif moves == 3:
            self.moves = ('Bubble', 'Water Pulse')
        elif moves == 4:
            self.moves = ('Tackle', 'Aqua Jet')
        elif moves == 5:
            self.moves = ('Tackle', 'Aqua Tail')
        else:
            self.moves = ('Tackle', 'Water Pulse')
#Generating size stats
        self.height = float(random.randint(40, 70))/100
        self.weight = float(random.randint(700,1100))/100
    
    def evolve(self, lvl):
        return Wartortle(self.name,self.cp, lvl)
