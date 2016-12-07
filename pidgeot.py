import random
class Pidgeot:
    poketype = ['Normal', 'Flying']
    description = 'This Pokemon has a dazzling plumage of beautifully glossy feathers. Many Trainers are captivated by the striking beauty of the feathers on its head, compelling them to choose Pidgeot as their Pokemon.'
    pokemon = 'Pidgeot'

    def __init__(self, name='Pidgeot', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(11, 20)/10)*startcp)
        if name == 'Pidgeotto':
            name = 'Pidgeot'
        self.attack = 170 + random.randint(1, 15)
        self.defense = 166 + random.randint(1, 15)
        self.cp = int((random.randint(15, 25)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Fly', 'Gust')
        elif moves == 2:
            self.moves = ('Fly', 'Twister')
        elif moves == 3:
            self.moves = ('Quick Attack', 'Gust')
        elif moves == 4:
            self.moves = ('Quick Attack', 'Twister')
        elif moves == 5:
            self.moves = ('Steel Wing', 'Gust')
        else:
            self.moves = ('Steel Wing', 'Twister')
#Generating size stats
        self.height = float(random.randint(140, 180))/100
        self.weight = float(random.randint(20000,50000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
