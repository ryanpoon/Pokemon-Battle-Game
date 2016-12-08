import random
class Alakazam:
    poketype = ['Psychic']
    description = "Alakazam's brain continually grows, making its head far too heavy to support with its neck. This Pokemon holds its head up using its psychokinetic power instead."
    pokemon = 'Alakazam'

    def __init__(self, name='Alakazam', startcp = None, level=1):
        if startcp == None:
            startcp = int(random.randint(10,level*29)*(random.randint(13, 17)/10))
        if name == 'Kadabra':
            name = 'Alakazam'
        self.attack = 271 + random.randint(1, 15)
        self.defense = 194 + random.randint(1, 15)
        self.stamina = 110 + random.randint(1, 15)
        self.cp = int((random.randint(14, 15)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Confusion', 'Dazzling Gleam')
        elif moves == 2:
            self.moves = ('Confusion', 'Psybeam')
        elif moves == 3:
            self.moves = ('Confusion', 'Shadow Ball')
        elif moves == 4:
            self.moves = ('Psycho Cut', 'Dazzling Gleam')
        elif moves == 5:
            self.moves = ('Psycho Cut', 'Psybeam')
        else:
            self.moves = ('Psycho Cut', 'Shadow Ball')
#Generating size stats
        self.height = float(random.randint(130, 170))/100
        self.weight = float(random.randint(3000,6600))/100
    
 

