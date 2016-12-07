import random
class Machamp:
    poketype = ['Fighting']
    description = "Machamp has the power to hurl anything aside. However, trying to do any work requiring care and dexterity causes its arms to get tangled. This Pokemon tends to leap into action before it thinks."
    pokemon = 'Machamp'

    def __init__(self, name='Machamp', startcp = None, level=1):
        if startcp == None:
            startcp = int((random.randint(15, 20)/10)*random.randint(10,level*30))
        if name == 'Machoke':
            name = 'Machamp'
        self.attack = 234 + random.randint(1, 15)
        self.defense = 162 + random.randint(1, 15)
        self.stamina = 180 + random.randint(1, 15)
        self.cp = int((random.randint(20, 28)/10)*startcp)
        self.name = name
        self.hp = int(self.cp/9)
        self.maxhp = int(self.cp/9)
#Generating moves
        moves = random.randint(1,7)
        if moves == 1:
            self.moves = ('Karate Chop', 'Cross Chop')
        elif moves == 2:
            self.moves = ('Karate Chop', 'Stone Edge')
        elif moves == 3:
            self.moves = ('Karate Chop', 'Submission')
        elif moves == 4:
            self.moves = ('Bullet Punch', 'Cross Chop')
        elif moves == 5:
            self.moves = ('Bullet Punch', 'Stone Edge')
        else:
            self.moves = ('Bullet Punch', 'Submission')
#Generating size stats
        self.height = float(random.randint(140, 180))/100
        self.weight = float(random.randint(10000,16000))/100
    
 

