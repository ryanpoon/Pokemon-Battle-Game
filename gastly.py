import random
from haunter import Haunter
class Gastly:
    poketype = ['Ghost', 'Poison']
    description = "Gastly is largely composed of gaseous matter. When exposed to a strong wind, the gaseous body quickly dwindles away. Groups of this Pokemon cluster under the eaves of houses to escape the ravages of wind."
    pokemon = 'Gastly'

    def __init__(self, name='Gastly', level=1):
        self.attack = 60 + random.randint(1, 15)
        self.defense = 186 + random.randint(1, 15)
        self.stamina = 70 + random.randint(1, 15)
        self.cp = random.randint(10, level*25)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Lick', 'Dark Pulse')
        elif moves == 2:
            self.moves = ('Lick', 'Ominous Wind')
        elif moves == 3:
            self.moves = ('Lick', 'Sludge Bomb')
        elif moves == 4:
            self.moves = ('Sucker Punch', 'Dark Pulse')
        elif moves == 5:
            self.moves = ('Sucker Punch', 'Ominous Wind')
        else:
            self.moves = ('Sucker Punch', 'Sludge Bomb')
#Generating size stats
        self.height = float(random.randint(100, 160))/100
        self.weight = float(random.randint(9,11))/100
    
    def evolve(self, lvl):
        return Haunter(self.name,self.cp, lvl)
