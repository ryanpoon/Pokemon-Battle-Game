import random
class Flareon:
    poketype = ['Fire']
    description = "Flareon's fluffy fur has a functional purpose-it releases heat into the air so that its body does not get excessively hot. This Pokemon's body temperature can rise to a maximum of 1,650 degrees Fahrenheit."
    pokemon = 'Flareon'

    def __init__(self, name='Flareon', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Eevee':
            name = 'Flareon'
        self.attack = 238 + random.randint(1, 15)
        self.defense = 178 + random.randint(1, 15)
        self.cp = int((random.randint(20, 30)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,4)
        if moves == 1:
            self.moves = ('Ember', 'Heat Wave')
        elif moves == 2:
            self.moves = ('Ember', 'Fire Blast')
        else:
            self.moves = ('Ember', 'Flamethrower')
#Generating size stats
        self.height = float(random.randint(70, 110))/100
        self.weight = float(random.randint(2000,3000))/100
    
    
