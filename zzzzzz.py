import random
class Aaaaaa:
    poketype = ['???']
    description = '???'
    pokemon = '???'
    def __init__(self, name='???', level=1):
        self.attack = 5000 + random.randint(1, 15)
        self.defense = 5000 + random.randint(1, 15)
        self.cp = random.randint(level*10, level*75)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('?a5', '???')
        elif moves == 2:
            self.moves = ('?a5', '?')
        elif moves == 3:
            self.moves = ('?a5', '??')
        elif moves == 4:
            self.moves = ('?b22', '???')
        elif moves == 5:
            self.moves = ('?b22', '??')
        else:
            self.moves = ('?b22', '?')
#Generating size stats
        self.height = "???"
        self.weight = "???"
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    
