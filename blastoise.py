import random
class Blastoise:
    poketype = ['Water']
    description = "Blastoise has water spouts that protrude from its shell. The water spouts are very accurate. They can shoot bullets of water with enough accuracy to strike empty cans from a distance of over 160 feet."
    pokemon = 'Blastoise'

    def __init__(self, name='Blastoise', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Wartortle':
            name = 'Blastoise'
        self.attack = 186 + random.randint(1, 15)
        self.defense = 222 + random.randint(1, 15)
        self.cp = int((random.randint(13, 17)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Bite', 'Flash Cannon')
        elif moves == 2:
            self.moves = ('Bite', 'Hydro Pump')
        elif moves == 3:
            self.moves = ('Bite', 'Ice Beam')
        elif moves == 4:
            self.moves = ('Water Gun', 'Flash Cannon')
        elif moves == 5:
            self.moves = ('Water Gun', 'Hydro Pump')
        else:
            self.moves = ('Water Gun', 'Ice Beam')
#Generating size stats
        self.height = float(random.randint(130, 190))/100
        self.weight = float(random.randint(6000,9000))/100
    
 
