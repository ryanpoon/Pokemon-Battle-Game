import random
class Pidgeot:
    poketype = ['Normal', 'Flying']
    description = 'This Pokemon has a dazzling plumage of beautifully glossy feathers. Many Trainers are captivated by the striking beauty of the feathers on its head, compelling them to choose Pidgeot as their Pokemon.'
    pokemon = 'Pidgeot'

    def __init__(self, name='Pidgeot', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(17, 19)/10)*random.randint(10, level*15))
        if name == 'Pidgeotto':
            name = 'Pidgeot'
        self.attack = 170 + random.randint(1, 15)
        self.defense = 166 + random.randint(1, 15)
        self.cp = int((random.randint(15, 18)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Steel Wing', 'Aerial Ace')
        elif moves == 2:
            self.moves = ('Steel Wing', 'Hurricane')
        elif moves == 3:
            self.moves = ('Steel Wing', 'Air Cutter')
        elif moves == 4:
            self.moves = ('Wing Attack', 'Aerial Ace')
        elif moves == 5:
            self.moves = ('Wing Attack', 'Air Cutter')
        else:
            self.moves = ('Wing Attack', 'Hurricane')
#Generating size stats
        self.height = float(random.randint(120, 180))/100
        self.weight = float(random.randint(2000,6000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
