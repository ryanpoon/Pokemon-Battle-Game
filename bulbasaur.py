import random
from ivysaur import Ivysaur
class Bulbasaur:
    poketype = ['Grass', 'Poison']
    description = "Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger."
    pokemon = 'Bulbasaur'

    def __init__(self, name='Bulbasaur', level=1):
        self.attack = 126 + random.randint(1, 15)
        self.defense = 126 + random.randint(1, 15)
        self.stamina = 90 + random.randint(1, 15)
        self.cp = random.randint(10, level*25)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Vine Whip', 'Power Whip')
        elif moves == 2:
            self.moves = ('Vine Whip', 'Seed Bomb')
        elif moves == 3:
            self.moves = ('Vine Whip', 'Sludge Bomb')
        elif moves == 4:
            self.moves = ('Tackle', 'Power Whip')
        elif moves == 5:
            self.moves = ('Tackle', 'Seed Bomb')
        else:
            self.moves = ('Tackle', 'Sludge Bomb')
#Generating size stats
        self.height = float(random.randint(5000, 9000))/100
        self.weight = float(random.randint(400,900))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    def evolve(self, lvl):
        return Ivysaur(self.name,self.cp, lvl)
