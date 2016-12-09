import random
class Exeggutor:
    poketype = ['Grass', 'Psychic']
    description = "Exeggutor originally came from the tropics. Its heads steadily grow larger from exposure to strong sunlight. It is said that when the heads fall off, they group together to form Exeggcute."
    pokemon = 'Exeggutor'

    def __init__(self, name='Exeggutor', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*23)
        if name == 'Exeggcute':
            name = 'Exeggutor'
        self.stamina = 190 + random.randint(1, 15)
        self.attack = 233 + random.randint(1, 15)
        self.defense = 158 + random.randint(1, 15)
        self.cp = int((random.randint(25, 31)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Confusion', 'Psychic')
        elif moves == 2:
            self.moves = ('Confusion', 'Seed Bomb')
        elif moves == 3:
            self.moves = ('Confusion', 'Solar Beam')
        elif moves == 4:
            self.moves = ('Zen Headbutt', 'Psychic')
        elif moves == 5:
            self.moves = ('Zen Headbutt', 'Solar Beam')
        else:
            self.moves = ('Zen Headbutt', 'Seed Bomb')
#Generating size stats
        self.height = float(random.randint(150, 250))/100
        self.weight = float(random.randint(10000,14000))/100
    
 
