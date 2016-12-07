import random
class Rhydon:
    poketype = ['Ground', 'Rock']
    description = "Rhydon's horn can crush even uncut diamonds. One sweeping blow of its tail can topple a building. This Pokemon's hide is extremely tough. Even direct cannon hits dont leave a scratch."
    pokemon = 'Rhydon'

    def __init__(self, name='Rhydon', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*30)
        if name == 'Rhyhorn':
            name = 'Rhydon'
        self.stamina = 190
        self.attack = 166 + random.randint(1, 15)
        self.defense = 160 + random.randint(1, 15)
        self.cp = int((random.randint(35, 40)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Mud Slap', 'Earthquake')
        elif moves == 2:
            self.moves = ('Mud Slap', 'Megahorn')
        elif moves == 3:
            self.moves = ('Mud Slap', 'Stone Edge')
        elif moves == 4:
            self.moves = ('Rock Smash', 'Earthquake')
        elif moves == 5:
            self.moves = ('Rock Smash', 'Megahorn')
        else:
            self.moves = ('Rock Smash', 'Stone Edge')
#Generating size stats
        self.height = float(random.randint(170, 230))/100
        self.weight = float(random.randint(9000,14000))/100
    
    
