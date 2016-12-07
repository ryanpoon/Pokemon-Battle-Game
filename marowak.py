import random
class Marowak:
    poketype = ['Ground']
    description = "Marowak is the evolved form of a Cubone that has overcome its sadness at the loss of its mother and grown tough. This Pokemon's tempered and hardened spirit is not easily broken."
    pokemon = 'Marowak'

    def __init__(self, name='Marowak', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*23)
        if name == 'Cubone':
            name = 'Marowak'
        self.stamina = 120 + random.randint(1, 15)
        self.attack = 144 + random.randint(1, 15)
        self.defense = 200 + random.randint(1, 15)
        self.cp = int((random.randint(12, 20)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Mud Slap', 'Dig')
        elif moves == 2:
            self.moves = ('Mud Slap', 'Earthquake')
        elif moves == 3:
            self.moves = ('Mud Slap', 'Bone Club')
        elif moves == 4:
            self.moves = ('Rock Smash', 'Earthquake')
        elif moves == 5:
            self.moves = ('Rock Smash', 'Dig')
        else:
            self.moves = ('Rock Smash', 'Bone Club')
#Generating size stats
        self.height = float(random.randint(50, 150))/100
        self.weight = float(random.randint(3000,6000))/100
    
 
