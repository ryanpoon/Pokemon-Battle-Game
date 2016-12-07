import random
class Venasaur:
    poketype = ['Grass', 'Poison']
    description = "There is a large flower on Venusaur's back. The flower is said to take on vivid colors if it gets plenty of nutrition and sunlight. The flower's aroma soothes the emotions of people."
    pokemon = 'Venasaur'

    def __init__(self, name='Venasaur', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(20, 30)/10)*random.randint(10,level*25))
        if name == 'Ivysaur':
            name = 'Venasaur'
        self.attack = 198 + random.randint(1, 15)
        self.defense = 200 + random.randint(1, 15)
        self.stamina = 160 + random.randint(1, 15)
        self.cp = int((random.randint(12, 18)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Razor Leaf', 'Power Whip')
        elif moves == 2:
            self.moves = ('Razor Leaf', 'Sludge Bomb')
        elif moves == 3:
            self.moves = ('Razor Leaf', 'Solar Beam')
        elif moves == 4:
            self.moves = ('Vine Whip', 'Power Whip')
        elif moves == 5:
            self.moves = ('Vine Whip', 'Sludge Bomb')
        else:
            self.moves = ('Vine Whip', 'Solar Beam')
#Generating size stats
        self.height = float(random.randint(150, 250))/100
        self.weight = float(random.randint(7000,13000))/100
    
 

