import random
class Charizard:
    poketype = ['Fire']
    description = "Charizard flies around the sky in search of powerful opponents. It breathes fire of such great heat that it melts anything. However, it never turns its fiery breath on any opponent weaker than itself.	"
    pokemon = 'Charizard'

    def __init__(self, name='Charizard', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(20, 30)/10)*random.randint(10,level*25))
        if name == 'Charmeleon':
            name = 'Charizard'
        self.attack = 212 + random.randint(1, 15)
        self.defense = 182 + random.randint(1, 15)
        self.stamina = 156 + random.randint(1, 15)
        self.cp = int((random.randint(12, 18)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Ember', 'Fire Blast')
        elif moves == 2:
            self.moves = ('Ember', 'Dragon Claw')
        elif moves == 3:
            self.moves = ('Ember', 'Flamethrower')
        elif moves == 4:
            self.moves = ('Wing Attack', 'Fire Blast')
        elif moves == 5:
            self.moves = ('Wing Attack', 'Dragon Claw')
        else:
            self.moves = ('Wing Attack', 'Flamethrower')
#Generating size stats
        self.height = float(random.randint(150, 190))/100
        self.weight = float(random.randint(7000,11000))/100
    
    def powerup(self, lvl):
        self.cp += lvl*2
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
