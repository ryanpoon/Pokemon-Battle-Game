import random
class Beedrill:
    poketype = ['Bug', 'Poison']
    description = 'Beedrill is extremely territorial. No one should ever approach its nest. This is for their own safety. If angered, they will attack in a furious swarm.'    
    pokemon = 'Beedrill'

    def __init__(self, name='Beedrill', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(10, 11)/10)*random.randint(10, level*15))
        if name == 'Kakuna':
            name = 'Beedrill'
        self.attack = 144 + random.randint(1, 15)
        self.defense = 130 + random.randint(1, 15)
        self.cp = int((random.randint(30, 40)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Bug Bite', 'Aerial Ace')
        elif moves == 2:
            self.moves = ('Bug Bite', 'Sludge Bomb')
        elif moves == 3:
            self.moves = ('Bug Bite', 'X-Scissor')
        elif moves == 4:
            self.moves = ('Poison Jab', 'Aerial Ace')
        elif moves == 5:
            self.moves = ('Poison Jab', 'Sludge Bomb')
        else:
            self.moves = ('Poison Jab', 'X-Scissor')
 
#Generating size stats
        self.height = float(random.randint(45, 75))/100
        self.weight = float(random.randint(500,1500))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    
