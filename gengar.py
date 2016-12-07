import random
class Gengar:
    poketype = ['Ghost', 'Poison']
    description = "Sometimes, on a dark night, your shadow thrown by a streetlight will suddenly and startlingly overtake you. It is actually a Gengar running past you, pretending to be your shadow."
    pokemon = 'Gengar'

    def __init__(self, name='Gengar', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(13, 21)/10)*random.randint(10,level*25))
        if name == 'Haunter':
            name = 'Gengar'
        self.attack = 120 + random.randint(1, 15)
        self.defense = 261 + random.randint(1, 15)
        self.stamina = 156 + random.randint(1, 15)
        self.cp = int((random.randint(13, 21)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Sucker Punch', 'Dark Pulse')
        elif moves == 2:
            self.moves = ('Sucker Punch', 'Shadow Ball')
        elif moves == 3:
            self.moves = ('Sucker Punch', 'Sludge Bomb')
        elif moves == 4:
            self.moves = ('Shadow Claw', 'Dark Pulse')
        elif moves == 5:
            self.moves = ('Shadow Claw', 'Shadow Ball')
        else:
            self.moves = ('Shadow Claw', 'Sludge Bomb')
#Generating size stats
        self.height = float(random.randint(100, 200))/100
        self.weight = float(random.randint(2000, 6000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    
