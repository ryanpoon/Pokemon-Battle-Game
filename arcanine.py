import random
class Arcanine:
    poketype = ['Fire']
    description = "Arcanine is known for its high speed. It is said to be capable of running over 6,200 miles in a single day and night. The fire that blazes wildly within this Pokemon's body is its source of power."
    pokemon = 'Arcanine'

    def __init__(self, name='Arcanine', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*29)
        if name == 'Growlithe':
            name = 'Arcanine'
        self.stamina = 180
        self.attack = 227 + random.randint(1, 15)
        self.defense = 166 + random.randint(1, 15)
        self.cp = int((random.randint(20, 25)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Bite', 'Bulldoze')
        elif moves == 2:
            self.moves = ('Bite', 'Fire Blast')
        elif moves == 3:
            self.moves = ('Bite', 'Flamethrower')
        elif moves == 4:
            self.moves = ('Fire Fang', 'Bulldoze')
        elif moves == 5:
            self.moves = ('Fire Fang', 'Fire Blast')
        else:
            self.moves = ('Fire Fang', 'Flamethrower')
#Generating size stats
        self.height = float(random.randint(170, 230))/100
        self.weight = float(random.randint(9000,14000))/100
    
    
