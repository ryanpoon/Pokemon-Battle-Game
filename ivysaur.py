import random
from venasaur import Venasaur
class Ivysaur:
    poketype = ['Grass', 'Poison']
    description = "There is a bud on this Pokemon's back. To support its weight, Ivysaur's legs and trunk grow thick and strong. If it starts spending more time lying in the sunlight, it's a sign that the bud will bloom into a large flower soon."
    pokemon = 'Ivysaur'

    def __init__(self, name='Ivysaur', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Bulbasaur':
            name = 'Ivysaur'
        self.attack = 156 + random.randint(1, 15)
        self.defense = 158 + random.randint(1, 15)
        self.stamina = 120 + random.randint(1, 15)
        self.cp = int((random.randint(20, 30)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Razor Leaf', 'Power Whip')
        elif moves == 2:
            self.moves = ('Razor Leaf', 'Sludge Bomb')
        elif moves == 3:
            self.moves = ('Razor Leaf', 'Solar Beam')
        elif moves == 4:
            self.moves = ('Vine Whip', 'Power Whip')
        elif moves == 5:
            self.moves = ('Vine Whip', 'Sludge Bomb')
        else:
            self.moves = ('Vine Whip', 'Solar Beam')
#Generating size stats
        self.height = float(random.randint(70, 130))/100
        self.weight = float(random.randint(1100,1300))/100
    
    
    def evolve(self, lvl):
        return Venasaur(self.name, self.cp, lvl)
