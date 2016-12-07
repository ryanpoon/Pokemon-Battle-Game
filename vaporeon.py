import random
class Vaporeon:
    poketype = ['Water']
    description = "Vaporeon underwent a spontaneous mutation and grew fins and gills that allow it to live underwater. This Pokemon has the ability to freely control water."
    pokemon = 'Vaporeon'

    def __init__(self, name='Vaporeon', startcp = None, level=1):
        if startcp == None:
            startcp = random.randint(10,level*25)
        if name == 'Eevee':
            name = 'Vaporeon'
        self.attack = 186 + random.randint(1, 15)
        self.defense = 168 + random.randint(1, 15)
        self.cp = int((random.randint(30, 40)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,4)
        if moves == 1:
            self.moves = ('Water Gun', 'Water Pulse')
        elif moves == 2:
            self.moves = ('Water Gun', 'Aqua Tail')
        else:
            self.moves = ('Water Gun', 'Hydro Pump')
#Generating size stats
        self.height = float(random.randint(70, 130))/100
        self.weight = float(random.randint(2500,3500))/100
    
    
