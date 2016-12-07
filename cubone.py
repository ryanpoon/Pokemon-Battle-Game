import random
from marowak import Marowak
class Cubone:
    poketype = ['Ground']
    description = 'Cubone pines for the mother it will never see again. Seeing a likeness of its mother in the full moon, it cries. The stains on the skull the Pokemon wears are made by the tears it sheds.'
    pokemon = 'Cubone'

    def __init__(self, name='Cubone', level=1):
        self.stamina = 100 + random.randint(1, 15)
        self.attack = 90 + random.randint(1, 15)
        self.defense = 165 + random.randint(1, 15)
        self.cp = random.randint(10, level*23)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Mud Slap', 'Bone Club')
        elif moves == 2:
            self.moves = ('Mud Slap', 'Dig')
        elif moves == 3:
            self.moves = ('Mud Slap', 'Bulldoze')
        elif moves == 4:
            self.moves = ('Rock Smash', 'Bone Club')
        elif moves == 5:
            self.moves = ('Rock Smash', 'Dig')
        else:
            self.moves = ('Rock Smash', 'Bull Doze')
#Generating size stats
        self.height = float(random.randint(20, 60))/100
        self.weight = float(random.randint(1000,2000))/100
    
    
    def evolve(self, lvl):
        return Marowak(self.name,self.cp, lvl)
