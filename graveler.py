import random
from golem import Golem
class Graveler:
    poketype = ['Rock', 'Ground']
    description = "Graveler grows by feeding on rocks. Apparently, it prefers to eat rocks that are covered in moss. This Pokemon eats its way through a ton of rocks on a daily basis."
    pokemon = 'Graveler'

    def __init__(self, name='Graveler', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10, level*30)
        if name == 'Geodude':
            name = 'Graveler'
        self.attack = 164 + random.randint(1, 15)
        self.defense = 196 + random.randint(1, 15)
        self.cp = int((random.randint(13, 15)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,5)
        if moves == 1:
            self.moves = ('Mud Slap', 'Dig')
        elif moves == 2:
            self.moves = ('Mud Slap', 'Rock Slide')
        elif moves == 3:
            self.moves = ('Mud Slap', 'Stone Edge')
        elif moves == 4:
            self.moves = ('Rock Throw', 'Dig')
        elif moves == 5:
            self.moves = ('Rock Throw', 'Rock Slide')
        else:
            self.moves = ('Rock Throw', 'Stone Edge')
#Generating size stats
        self.height = float(random.randint(80, 120))/100
        self.weight = float(random.randint(9000,11000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Golem(self.name, self.cp, lvl)
