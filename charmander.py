import random
from charmeleon import Charmeleon
class Charmander:
    poketype = ['Fire']
    description = "The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when Charmander is enjoying itself. If the Pokemon becomes enraged, the flame burns fiercely."
    pokemon = 'Charmander'

    def __init__(self, name='Charmander', level=1):
        self.attack = 128 + random.randint(1, 15)
        self.defense = 108 + random.randint(1, 15)
        self.stamina = 78 + random.randint(1, 15)
        self.cp = random.randint(10, level*25)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Ember', 'Flame Burst')
        elif moves == 2:
            self.moves = ('Ember', 'Flame Charge')
        elif moves == 3:
            self.moves = ('Ember', 'Flamethrower')
        elif moves == 4:
            self.moves = ('Scratch', 'Flame Burst')
        elif moves == 5:
            self.moves = ('Scratch', 'Flame Charge')
        else:
            self.moves = ('Scratch', 'Flamethrower')
#Generating size stats
        self.height = float(random.randint(400, 800))/100
        self.weight = float(random.randint(600,1200))/100
    
    def evolve(self, lvl):
        return Charmeleon(self.name,self.cp, lvl)
