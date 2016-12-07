import random
from machamp import Machamp
class Machoke:
    poketype = ['Fighting']
    description = "Machoke's thoroughly toned muscles possess the hardness of steel. This Pokemon has so much strength, it can easily hold aloft a sumo wrestler on just one finger."
    pokemon = 'Machoke'

    def __init__(self, name='Machoke', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10, level*30)
        if name == 'Machop':
            name = 'Machoke'
        self.attack = 177 + random.randint(1, 15)
        self.defense = 130 + random.randint(1, 15)
        self.cp = int((random.randint(15, 20)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Karate Chop', 'Brick Break')
        elif moves == 2:
            self.moves = ('Karate Chop', 'Cross Chop')
        elif moves == 3:
            self.moves = ('Karate Chop', 'Submission')
        elif moves == 4:
            self.moves = ('Low Kick', 'Brick Break')
        elif moves == 5:
            self.moves = ('Low Kick', 'Cross Chop')
        else:
            self.moves = ('Low Kick', 'Submission')
#Generating size stats
        self.height = float(random.randint(130, 170))/100
        self.weight = float(random.randint(6000,8000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Machamp(self.name, self.cp, lvl)
