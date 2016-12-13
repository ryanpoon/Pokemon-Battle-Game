import random
class Golem:
    poketype = ['Rock', 'Ground']
    description = "Golem live up on mountains. If there is a large earthquake, these Pokemon will come rolling down off the mountains en masse to the foothills below."
    pokemon = 'Golem'

    def __init__(self, name='Golem', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(13, 15)/10)*random.randint(10,level*30))
        if name == 'Graveler':
            name = 'Golem'
        self.attack = 211 + random.randint(1, 15)
        self.defense = 229 + random.randint(1, 15)
        self.stamina = 160 + random.randint(1, 15)
        self.cp = int((random.randint(14, 17)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Mud Slap', 'Ancient Power')
        elif moves == 2:
            self.moves = ('Mud Slap', 'Earthquake')
        elif moves == 3:
            self.moves = ('Mud Slap', 'Stone Edge')
        elif moves == 4:
            self.moves = ('Rock Throw', 'Ancient Power')
        elif moves == 5:
            self.moves = ('Rock Throw', 'Earthquake')
        else:
            self.moves = ('Rock Throw', 'Stone Edge')
#Generating size stats
        self.height = float(random.randint(120, 160))/100
        self.weight = float(random.randint(20000, 40000))/100
    
 

