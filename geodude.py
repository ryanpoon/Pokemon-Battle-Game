import random
from graveler import Graveler
class Geodude:
    poketype = ['Rock', 'Ground']
    description = "The longer a Geodude lives, the more its edges are chipped and worn away, making it more rounded in appearance. However, this Pokemon's heart will remain hard, craggy, and rough always."
    pokemon = 'Geodude'

    def __init__(self, name='Geodude', level=1):
        self.attack = 132 + random.randint(1, 15)
        self.defense = 163 + random.randint(1, 15)
        self.stamina = 80 + random.randint(1, 15)
        self.cp = random.randint(10, level*30)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Rock Throw', 'Dig')
        elif moves == 2:
            self.moves = ('Rock Throw', 'Rock Slide')
        elif moves == 3:
            self.moves = ('Rock Throw', 'Rock Tomb')
        elif moves == 4:
            self.moves = ('Tackle', 'Dig')
        elif moves == 5:
            self.moves = ('Tackle', 'Rock Slide')
        else:
            self.moves = ('Tackle', 'Rock Tomb')
#Generating size stats
        self.height = float(random.randint(20, 60))/100
        self.weight = float(random.randint(1000,3000))/100
    
    def evolve(self, lvl):
        return Graveler(self.name,self.cp, lvl)
