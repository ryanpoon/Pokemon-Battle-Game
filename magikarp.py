from gyarados import Gyarados
import random
class Magikarp:
    poketype = ['Water']
    description = "Magikarp is a medium-sized fish Pokemon with large, heavy reddish-orange scales.\nIt has large, vacant eyes and pink lips."
    pokemon = 'Magikarp'

    def __init__(self, name='Magikarp', level = 1):
        self.attack = 42 + random.randint(1, 15)
        self.defense = 82 + random.randint(1, 15)
        self.cp = random.randint(10, (level*5)+5)
        self.name = name
        self.maxhp = int(self.cp/9)
        self.hp = int(self.cp/9)
        self.moves = ('Splash', 'Struggle')
		#Generating size stats
        
        self.height = float(random.randint(50,100))/100
        self.weight = float(random.randint(1000,1500))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.maxhp = int(self.cp/9)
        self.hp = int(self.cp/9)
    def evolve(self, lvl):
        return Gyarados(self.name, self.cp, lvl)
