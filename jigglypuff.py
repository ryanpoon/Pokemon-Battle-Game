import random
from wigglytuff import Wigglytuff
class Jigglypuff:
    poketype = ['Normal']
    description = "Jigglypuff's vocal cords can freely adjust the wavelength of its voice. This Pokemon uses this ability to sing at precisely the right wavelength to make its foes most drowsy."
    pokemon = 'Jigglypuff'

    def __init__(self, name='Jigglypuff', level=1):
        self.attack = 80 + random.randint(1, 15)
        self.defense = 44 + random.randint(1, 15)
        self.stamina = 230 + random.randint(1, 15)
        self.cp = random.randint(10, level*18)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Pound', 'Body Slam')
        elif moves == 2:
            self.moves = ('Pound', 'Dazzling Gleam')
        elif moves == 3:
            self.moves = ('Pound', 'Disarming Voice')
        elif moves == 4:
            self.moves = ('Feint Attack', 'Body Slam')
        elif moves == 5:
            self.moves = ('Feint Attack', 'Dazzling Gleam')
        else:
            self.moves = ('Feint Attack', 'Disarming Voice')
#Generating size stats
        self.height = float(random.randint(30, 70))/100
        self.weight = float(random.randint(400, 650))/100
    
    def evolve(self, lvl):
        return Wigglytuff(self.name,self.cp, lvl)
