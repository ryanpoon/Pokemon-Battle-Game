import random
class Dragonite:
    poketype = ['Dragon', 'Flying']
    description = "Dragonite is capable of circling the globe in just 16 hours. It is a kindhearted Pokemon that leads lost and foundering ships in a storm to the safety of land."
    pokemon = 'Dragonite'

    def __init__(self, name='Dragonite', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(15, 25)/10)*random.randint(10, level*21))
        if name == 'Dragonair':
            name = 'Dragonite'
        self.attack = 263 + random.randint(1, 15)
        self.defense = 201 + random.randint(1, 15)
        self.cp = int((random.randint(20, 24)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Dragon Breath', 'Dragon Claw')
        elif moves == 2:
            self.moves = ('Dragon Breath', 'Dragon Pulse')
        elif moves == 3:
            self.moves = ('Dragon Breath', 'Hyper Beam')
        elif moves == 4:
            self.moves = ('Steel Wing', 'Dragon Claw')
        elif moves == 5:
            self.moves = ('Steel Wing', 'Dragon Pulse')
        else:
            self.moves = ('Steel Wing', 'Hyper Beam')
#Generating size stats
        self.height = float(random.randint(160, 280))/100
        self.weight = float(random.randint(15000,25000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
