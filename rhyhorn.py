import random
from rhydon import Rhydon
class Rhyhorn:
    poketype = ['Ground', 'Rock']
    description = 'Rhyhorn runs in a straight line, smashing everything in its path. It is not bothered even if it rushes headlong into a block of steel. This Pokemon may feel some pain from the collision the next day, however.'
    pokemon = 'Rhyhorn'

    def __init__(self, name='Rhyhorn', level=1):
        self.attack = 110 + random.randint(1, 15)
        self.defense = 116 + random.randint(1, 15)
        self.stamina = 160 + random.randint(1, 15)
        self.cp = random.randint(10, level*30)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,5)
        if moves == 1:
            self.moves = ('Mud Slap', 'Bulldoze')
        elif moves == 2:
            self.moves = ('Mud Slap', 'Horn Attack')
        elif moves == 3:
            self.moves = ('Rock Smash', 'Bulldoze')
        else:
            self.moves = ('Rock Smash', 'Horn Attack')
#Generating size stats
        self.height = float(random.randint(70, 130))/100
        self.weight = float(random.randint(9000,12500))/100
    
    def evolve(self, lvl):
        return Rhydon(self.name,self.cp, lvl)
