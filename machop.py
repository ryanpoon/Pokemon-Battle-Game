import random
from machoke import Machoke
class Machop:
    poketype = ['Fighting']
    description = "Machop's muscles are special—they never get sore no matter how much they are used in exercise. This Pokemon has sufficient power to hurl a hundred adult humans."
    pokemon = 'Machp'

    def __init__(self, name='Machop', level=1):
        self.attack = 137 + random.randint(1, 15)
        self.defense = 88 + random.randint(1, 15)
        self.stamina = 140 + random.randint(1, 15)
        self.cp = random.randint(10, level*30)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Karate Chop', 'Cross Chop')
        elif moves == 2:
            self.moves = ('Karate Chop', 'Brick Break')
        elif moves == 3:
            self.moves = ('Karate Chop', 'Low Sweep')
        elif moves == 4:
            self.moves = ('Low Kick', 'Cross Chop')
        elif moves == 5:
            self.moves = ('Low Kick', 'Brick Break')
        else:
            self.moves = ('Low Kick', 'Low Sweep')
#Generating size stats
        self.height = float(random.randint(60, 100))/100
        self.weight = float(random.randint(1000,3000))/100
    
    def evolve(self, lvl):
        return Machoke(self.name,self.cp, lvl)
