import random
from arcanine import Arcanine
class Growlithe:
    poketype = ['Fire']
    description = "Growlithe has a superb sense of smell. Once it smells anything, this Pokemon won't forget the scent, no matter what. It uses its advanced olfactory sense to determine the emotions of other living things."
    pokemon = 'Growlithe'

    def __init__(self, name='Growlithe', level=1):
        self.attack = 136 + random.randint(1, 15)
        self.defense = 96 + random.randint(1, 15)
        self.stamina = 110 + random.randint(1, 15)
        self.cp = random.randint(10, level*28)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Bite', 'Body Slam')
        elif moves == 2:
            self.moves = ('Bite', 'Flame Wheel')
        elif moves == 3:
            self.moves = ('Bite', 'Flamethrower')
        elif moves == 4:
           self.moves = ('Ember', 'Body Slam')
        elif moves == 5:
           self.moves = ('Ember', 'Flame Wheel')
        else:
            self.moves = ('Ember', 'Flamethrower')
#Generating size stats
        self.height = float(random.randint(50, 90))/100
        self.weight = float(random.randint(1500,2300))/100
    
    def evolve(self, lvl):
        return Arcanine(self.name,self.cp, lvl)
