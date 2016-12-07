import random
class Jolteon:
    poketype = ['Electric']
    pokemon = 'Jolteon'
    description = "Jolteon's cells generate a low level of electricity. This power is amplified by the static electricity of its fur, enabling the Pokemon to drop thunderbolts. The bristling fur is made of electrically charged needles."
    def __init__(self, name='Jolteon', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Eevee':
            name = 'Jolteon'
        self.attack = 192 + random.randint(1, 15)
        self.defense = 174 + random.randint(1, 15)
        self.cp = int((random.randint(15, 20)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,4)
        if moves == 1:
            self.moves = ('Thunder Shock', 'Discharge')
        elif moves == 2:
            self.moves = ('Thunder Shock', 'Thunderbolt')
        else:
            self.moves = ('Thunder Shock', 'Thunder')
#Generating size stats
        self.height = float(random.randint(40, 100))/100
        self.weight = float(random.randint(2000,3000))/100
    
    
