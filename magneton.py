import random
class Magneton:
    poketype = ['Electric', 'Steel']
    description = "Magneton emits a powerful magnetic force that is fatal to mechanical devices. As a result, large cities sound sirens to warn citizens of large-scale outbreaks of this Pokemon."
    pokemon = 'Magneton'
    def __init__(self, name='Magneton', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10, level*27)
        if name == 'Magnemite':
            name = 'Magneton'
        self.attack = 223 + random.randint(1, 15)
        self.defense = 182 + random.randint(1, 15)
        self.cp = int(random.randint(18,21)/10*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Spark', 'Discharge')
        elif moves == 2:
            self.moves = ('Spark', 'Magnet Bomb')
        elif moves == 3:
            self.moves = ('Spark', 'Flash Cannon')
        elif moves == 4:
            self.moves = ('Thunder Shock', 'Discharge')
        elif moves == 5:
            self.moves = ('Thunder Shock', 'Magnet Bomb')
        else:
            self.moves = ('Thunder Shock', 'Flash Cannon')
#Generating size stats
        self.height = float(heightpossibility)/100
        self.weight = float(weightpossibility)/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
