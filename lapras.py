import random
class Lapras:
    poketype = ['Water', 'Ice']
    description = 'People have driven Lapras almost to the point of extinction. In the evenings, this Pokemon is said to sing plaintively as it seeks what few others of its kind still remain.'
    pokemon = 'Lapras'
    def __init__(self, name='Lapras', level=1):
        self.attack = 186 + random.randint(1, 15)
        self.defense = 190 + random.randint(1, 15)
        self.cp = random.randint(10, level*80)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Frost Breath', 'Blizzard')
        elif moves == 2:
            self.moves = ('Frost Breath', 'Dragon Pulse')
        elif moves == 3:
            self.moves = ('Frost Breath', 'Ice Beam')
        elif moves == 4:
            self.moves = ('Ice Shard', 'Blizzard')
        elif moves == 5:
            self.moves = ('Ice Shard', 'Dragon Pulse')
        else:
            self.moves = ('Ice Shard', 'Ice Beam')
#Generating size stats
        self.height = float(random.randint(180, 250))/100
        self.weight = float(random.randint(15000,25000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
    
