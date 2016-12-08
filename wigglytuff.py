import random
class Wigglytuff:
    poketype = ['Normal']
    pokemon = 'Wigglytuff'
    description = "Wigglytuff has large, saucerlike eyes. The surfaces of its eyes are always covered with a thin layer of tears. If any dust gets in this Pokemon's eyes, it is quickly washed away."
    def __init__(self, name='Wigglytuff', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*18)
        if name == 'Jigglypuff':
            name = 'Wigglytuff'
        self.attack = 156 + random.randint(1, 15)
        self.defense = 93 + random.randint(1, 15)
        self.cp = int((random.randint(20, 26)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Feint Attack', 'Hyper Beam')
        elif moves == 2:
            self.moves = ('Feint Attack', 'Play Rough')
        elif moves == 3:
            self.moves = ('Feint Attack', 'Dazzling Gleam')
        elif moves == 4:
            self.moves = ('Pound', 'Dazzling Gleam')
        elif moves == 5:
            self.moves = ('Pound', 'Play Rough')
        else:
            self.moves = ('Pound', 'Hyper Beam')
#Generating size stats
        self.height = float(random.randint(75, 125))/100
        self.weight = float(random.randint(900,1500))/100
    
    
