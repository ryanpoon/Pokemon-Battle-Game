import random
class Raichu:
    poketype = ['Electric']
    description = 'Raichu is the evolved form of Pikachu.'
    pokemon = 'Raichu'

    def __init__(self, name='Raichu', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Pikachu':
            name = 'Raichu'
        self.stamina = 120 + random.randint(1, 15)
        self.attack = 200 + random.randint(1, 15)
        self.defense = 154 + random.randint(1, 15)
        self.cp = int((random.randint(20, 30)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Spark', 'Thunder')
        elif moves == 2:
            self.moves = ('Spark', 'Brick Break')
        elif moves == 3:
            self.moves = ('Thunder Shock', 'Thunder')
        elif moves == 4:
            self.moves = ('Thunder Shock', 'Brick Break')
        elif moves == 5:
            self.moves = ('Quick Attack', 'Thunder')
        else:
            self.moves = ('Quick Attack', 'Brick Break')
#Generating size stats
        self.height = float(random.randint(100, 160))/100
        self.weight = float(random.randint(4000,7500))/100
    
 
