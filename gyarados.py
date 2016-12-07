import random
class Gyarados:
    poketype = ['Water', 'Flying']
    description = "When Magikarp evolves into Gyarados, its brain cells undergo a structural transformation. It is said that this transformation is to blame for this Pokemon's wildly violent nature."
    pokemon = 'Gyarados'

    def __init__(self, name='Gyarados', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10, level*5+5)
        if name == 'Magikarp':
            name = 'Gyarados'
        self.attack = 192 + random.randint(1, 15)
        self.defense = 196 + random.randint(1, 15)
        self.cp = int((random.randint(100, 150)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,4)
        if moves == 1:
            self.moves = ('Bite', 'Dragon Pulse')
        elif moves == 2:
            self.moves = ('Bite', 'Hydro Pump')
        else:
            self.moves = ('Bite', 'Twister')
#Generating size stats
        self.height = float(random.randint(600, 800))/100
        self.weight = float(random.randint(10000,30000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
