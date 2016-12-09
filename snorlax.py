import random
class Snorlax:
    poketype = ['Normal']
    description = "Snorlax's typical day consists of nothing more than eating and sleeping. It is such a docile Pokemon that there are children who use its expansive belly as a place to play."
    pokemon = 'Snorlax'
    def __init__(self, name='Snorlax', level=1):
        self.attack = 190 + random.randint(1, 15)
        self.defense = 190 + random.randint(1, 15)
        self.cp = random.randint(10, level*84)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Lick', 'Earthquake')
        elif moves == 2:
            self.moves = ('Lick', 'Hyper Beam')
        elif moves == 3:
            self.moves = ('Lick', 'Body Slam')
        elif moves == 4:
            self.moves = ('Zen Headbutt', 'Earthquake')
        elif moves == 5:
            self.moves = ('Zen Headbutt', 'Hyper Beam')
        else:
            self.moves = ('Zen Headbutt', 'Body Slam')
#Generating size stats
        self.height = float(random.randint(180, 250))/100
        self.weight = float(random.randint(40000,52000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    
