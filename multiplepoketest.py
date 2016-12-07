import random, sys, time, pyglet
weakness = {'Normal':('Fighting'),'Flying':('Ice', 'Electric', 'Rock'), 'Water':('Electric', 'Grass'), 'Fire':('Water', 'Rock', 'Ground'), 'Grass':('Fire', 'Poison', 'Bug', 'Ice', 'Flying'), 'Bug':('Fire', 'Flying'), 'Ice':('Fire'), 'Rock':('Water', 'Grass', 'Ground', 'Fighting', 'Steel'), 'Ground':('Water', 'Grass', 'Fighting'), 'Electric':('Ground', 'Rock'), 'Psychic':('Bug', 'Ghost'), 'Fighting':('Psychic, FLying'), 'Poison':('Psychic', 'Ground'), 'Steel':('Ground'), 'Bug':('Rock'), 'Ice':('Rock', 'Steel'), 'Ghost':('Ghost'), 'Dragon':('Dragon', 'Ice')}
def betterprint(string='', speed=.01, end='\n'):
    for i in range(len(string)-1):
        time.sleep(speed)
        print(string[i], end='')
    print(string[i+1], end = end)
def damage(hp, newhp, maxhp, name):
    dealt = hp-newhp
    if newhp<0:
        newhp = 0
    betterprint('{}: {}/{}'.format(name, hp, maxhp))
    print(' '*(len(name)+2), end='')
    betterprint('-{}'.format(dealt))
    betterprint('{}: {}/{}'.format(name, newhp, maxhp))

def iswin(pokelist1, pokelist2):
    poke1 = False
    for x in pokelist1:
        if pokelist1[x][0].hp > 0:
            poke1 = True
            break
    poke2 = False
    for x in pokelist2:
        if pokelist2[x][0].hp > 0:
            poke2 = True
            break
    if poke1 and poke2:
        return 0
    elif poke1:
        return 1
    else:
        return 2
        
    
def switch(pokelist1, pokelist2, weakness1, weakness2, poke1, poke2, num1, num2, num3, pokelist, pp1, pp2):
    
    if pokelist == 1:
        num4 = num2
        num1 = num3
        pokelist1[num4][1] = pp1
        pokelist1[num4][0] = poke1
        poke1 = pokelist1[num3][0]
        pp1 = pokelist1[num3][1]
        weakness1 = []
        for x in poke1.poketype:
            for y in weakness[x]:
                weakness1.append(y)
    else:
        num4 = num2
        num2 = num3
        pokelist2[num4][1] = pp2
        pokelist2[num4][0] = poke2
        poke2 = pokelist2[num3][0]
        pp2 = pokelist2[num3][1]
        weakness2 = []
        for x in poke2.poketype:
            for y in weakness[x]:
                weakness2.append(y)
    return(weakness1, weakness2, poke1, poke2, num1, num2, num3, pokelist, pp1, pp2)
def attack(attacker, defender, choice1, choice2, moveinfo, weakness1, weakness2):
    global damage
    betterprint(attacker.name+' used '+ attacker.moves[choice1]+'!')
    poker = attacker
    pokey = defender
    #if it is super effective
    if moveinfo[poker.moves[choice1]][1] in weakness2:
        oldhp = pokey.hp
        pokey.hp -= 1+int(((poker.cp+(poker.attack))/((750+(pokey.defense))*1.5))*(moveinfo[pokey.moves[choice1]][0]*1.5))
        damage(oldhp, pokey.hp, pokey.maxhp, pokey.name)
        betterprint('''It's super effective!''')
        if pokey.hp < 1:
            return (1, 0, 0)
    else:
        oldhp = pokey.hp
        pokey.hp -=1+int(((poker.cp+(poker.attack))/((750+(pokey.defense))*1.5))*(moveinfo[poker.moves[choice1]][0]))
        damage(oldhp, pokey.hp, pokey.maxhp, pokey.name)
        if pokey.hp < 1:
            return (1, 0, 0)
    betterprint(pokey.name+' used '+ pokey.moves[choice2]+'!')
    #if it is super effective
    if moveinfo[pokey.moves[choice2]][1] in weakness1:
        oldhp = poker.hp
        poker.hp -= 1+int(((pokey.cp+(pokey.attack))/((750+(poker.defense))*1.5))*(moveinfo[poker.moves[choice2]][0]*1.5))
        damage(oldhp, poker.hp, poker.maxhp, poker.name) 
        betterprint('''It's super effective!''')
        if poker.hp < 1:
            return (2, 0, 0)
    else:
        oldhp = poker.hp
        poker.hp -=1+int(((pokey.cp+(pokey.attack))/((750+(poker.defense))*1.5))*(moveinfo[pokey.moves[choice2]][0]))
        damage(oldhp, poker.hp, poker.maxhp, poker.name)
        if poker.hp < 1:
            return (2, 0, 0)
    return (0, poker.hp, pokey.hp)
    betterprint('Press Enter to Continue', end = ' ')
    confirm = input('')
def fight(pokelist1, pokelist2, moveinfo):
##    music = pyglet.resource.media('battlemusic.wav')
##    music.play()
##    pyglet.app.run()
    poke1 = pokelist1[0][0]
    poke2 = pokelist2[0][0]
    pp1 = pokelist1[0][1]
    pp2 = pokelist2[0][1]
    num1 = 0
    num2 = 0
    weakness1 = []
    weakness2 = []
    for x in poke1.poketype:
        for y in weakness[x]:
            weakness1.append(y)
    for x in poke2.poketype:
        for y in weakness[x]:
            weakness2.append(y)
    while True:
        print('-------------------------------------------------------------')
        betterprint(poke1.name+'('+poke1.pokemon+'): '+str(poke1.hp)+'/'+str(poke1.maxhp)+'\n'+poke2.name+'('+poke2.pokemon+'): '+str(poke2.hp)+'/'+str(poke2.maxhp))
        print('-------------------------------------------------------------')
        betterprint(poke1.name+''''s Moves:\n'''+'1. '+poke1.moves[0]+ ' PP: '+str(pp1[0])+'/'+str(moveinfo[poke1.moves[0]][2])+'\n2. '+poke1.moves[1]+ ' PP: '+str(pp1[1])+'/'+str(moveinfo[poke1.moves[1]][2]))
        switch1 = False
        while True:
            if pp1[0] == 0 and pp1[1] == 0:
                choice1 = None
                break
            betterprint('Which move do you want to use? Pick 1 or 2. You can switch with 3', end='')
            choice1 = input('')
            try:
                value = int(choice1)
            except ValueError:
                betterprint('Please put in a number!')
            else:
                choice1 = int(choice1)
                choice1-=1
                if choice1 == 2:
                    while True:
                        betterprint('Choose a pokemon:\n')
                        for x in range(len(pokelist1)):
                            poke = pokelist1[x][0]
                            betterprint('{}. {}  {}/{}'.format(x+1, poke.name, poke.hp, poke.maxhp))
                        choice = input()
                        try:
                            value = int(choice)
                        except ValueError:
                            betterprint('Please put in a number!')
                        else:
                            choice = int(choice)
                            if choice < 1 or choice > len(pokelist1):
                                betterprint('Please use a number that is in between 1 - {}'.format(len(poke2list)))
                            else:
                                choice -= 1
                                choice1 = choice
                                break
    
                    weakness1, weakness2, poke1, poke2, num1, num2, choice, pokelist, pp1, pp2 = switch(pokelist1, pokelist2, weakness1, weakness2, poke1, poke2, num1, num2, choice, 1, pp1, pp2)
                    switch1 = True
                    break
                elif choice1+1>2 or choice1+1<1:
                    betterprint('Please pick a number that is 1 or 2!')
                
                elif pp1[choice1] == 0:
                    betterprint('Out of PP!')
                else:
                    break
        print('\n'*50+'-------------------------------------------------------------\nIt is now player 2s turn.')
        betterprint(poke1.name+'('+poke1.pokemon+'): '+str(poke1.hp)+'/'+str(poke1.maxhp)+'\n'+poke2.name+'('+poke2.pokemon+'): '+str(poke2.hp)+'/'+str(poke2.maxhp))
        print('-------------------------------------------------------------')
        betterprint(poke2.name+''''s Moves:\n'''+'1. '+poke2.moves[0]+ ' PP: '+str(pp2[0])+'/'+str(moveinfo[poke2.moves[0]][2])+'\n2. '+poke2.moves[1]+ ' PP: '+str(pp2[1])+'/'+str(moveinfo[poke2.moves[1]][2]))
        switch2 = False
        while True:
            if pp2[0] == 0 and pp2[1] == 0:
                choice2 = None
            betterprint('Which move do you want to use? Pick 1 or 2. You can switch with 3.', end='')
            choice2 = input('')
            try:
                value = int(choice2)
            except ValueError:
                betterprint('Please put in a number!')
            else:
                choice2 = int(choice2)
                choice2 -= 1
                if choice2 == 2:
                    while True:
                        betterprint('Choose a pokemon:\n')
                        for x in range(len(pokelist2)):
                            poke = pokelist2[x][0]
                            betterprint('{}. {}  {}/{}\n'.format(x+1, poke.name, poke.hp, poke.maxhp))
                        choice = input()
                        try:
                            value = int(choice)
                        except ValueError:
                            betterprint('Please put in a number!')
                        else:
                            choice = int(choice)
                            if choice < 1 or choice > len(pokelist2):
                                betterprint('Please use a number that is in between 1 - {}'.format(len(poke2list)))
                            else:
                                choice -= 1
                                choice2 = choice
                                break
                    switch2 = True
                    weakness1, weakness2, poke1, poke2, num1, num2, num3, pokelist, pp1, pp2 = switch(pokelist1, pokelist2, weakness1, weakness2, poke1, poke2, num1, num2, choice,  2, pp1, pp2)
                    break
                elif choice2+1>2 or choice2+1<1:
                    betterprint('Please pick a number that is 1 - 3!')
                
                elif pp2[choice2] ==0:
                    betterprint('Out of PP!')
                else:
                    break
        betterprint('Press Enter to Continue', end = ' ')
        confirm = input('')
        print('\n'*50+'-------------------------------------------------------------\nTime for battle!')
        if switch1 == False:
            pp1[choice1] -= 1
        if switch2 == False:
            pp2[choice2] -= 1
        if switch1 == False and switch2 == False:
            pass
        elif switch2 == False:
            if moveinfo[poke2.moves[choice2]][1] in weakness1:
                oldhp = poke1.hp
                poke1.hp -= 1+int(((poke2.cp+(poke2.attack))/((750+(poke1.defense))*1.5))*(moveinfo[poke1.moves[choice2]][0]*1.5))
                damage(oldhp, poke1.hp, poke1.maxhp, poke1.name)
                betterprint('''It's super effective!''')
                if poke1.hp < 1:
                    if iswin(pokelist1, pokelist2) == 2:
                        break
                    else:
                        while True:
                            betterprint('Choose a pokemon:\n')
                            for x in range(len(pokelist2)):
                                poke = pokelist2[x][0]
                                betterprint('{}. {}  {}/{}\n'.format(x+1, poke.name, poke.hp, poke.maxhp))
                            choice = input()
                            try:
                                value = int(choice)
                            except ValueError:
                                betterprint('Please put in a number!')
                            else:
                                choice = int(choice)
                                if choice < 1 or choice > len(pokelist2):
                                    betterprint('Please use a number that is in between 1 - {}'.format(len(poke2list)))
                                else:
                                    break
                        
                        weakness1, weakness2, poke1, poke2, num1, num2, num3, pokelist, pp1, pp2 = switch(pokelist1, pokelist2, weakness1, weakness2, poke1, poke2, num1, num2, choice,  1, pp1, pp2)
            else:
                oldhp = poke1.hp
                poke1.hp -= 1+int(((poke2.cp+(poke2.attack))/((750+(poke1.defense))*1.5))*(moveinfo[poke1.moves[choice2]][0]))
                damage(oldhp, poke1.hp, poke1.maxhp, poke1.name)
                if poke1.hp < 1:
                    if iswin(pokelist1, pokelist2) == 2:
                        break
                    else:
                        while True:
                            betterprint('Choose a pokemon:\n')
                            for x in range(len(pokelist2)):
                                poke = pokelist2[x][0]
                                betterprint('{}. {}  {}/{}\n'.format(x+1, poke.name, poke.hp, poke.maxhp))
                            choice = input()
                            try:
                                value = int(choice)
                            except ValueError:
                                betterprint('Please put in a number!')
                            else:
                                choice = int(choice)
                                if choice < 1 or choice > len(pokelist2):
                                    betterprint('Please use a number that is in between 1 - {}'.format(len(poke2list)))
                                else:
                                    choice -= 1
                                    break
                        
                        weakness1, weakness2, poke1, poke2, num1, num2, num3, pokelist, pp1, pp2 = switch(pokelist1, pokelist2, weakness1, weakness2, poke1, poke2, num1, num2, choice, 1, pp1, pp2)
            betterprint(poke2.name+' used '+ poke2.moves[choice2]+'!')
        elif switch1 == False:
            if moveinfo[poke1.moves[choice1-1]][1] in weakness2:
                oldhp = poke2.hp
                poke2.hp -= 1+int(((poke1.cp+(poke1.attack))/((750+(poke2.defense))*1.5))*(moveinfo[poke2.moves[choice1]][0]*1.5))
                damage(oldhp, poke2.hp, poke2.maxhp, poke2.name)
                betterprint('''It's super effective!''')
                if poke2.hp < 1:
                    if iswin(pokelist1, pokelist2) == 1:
                        break
                    else:
                        while True:
                            betterprint('Choose a pokemon:\n')
                            for x in range(len(pokelist1)):
                                poke = pokelist1[x][0]
                                betterprint('{}. {}  {}/{}\n'.format(x+1, poke.name, poke.hp, poke.maxhp))
                            choice = input()
                            try:
                                value = int(choice)
                            except ValueError:
                                betterprint('Please put in a number!')
                            else:
                                choice = int(choice)
                                if choice < 1 or choice > len(pokelist1):
                                    betterprint('Please use a number that is in between 1 - {}'.format(len(poke1list)))
                                else:
                                    choice -= 1
                                    break
                        
                        weakness1, weakness2, poke1, poke2, num1, num2, num3, pokelist, pp1, pp2 = switch(pokelist1, pokelist2, weakness1, weakness2, poke1, poke2, num1, num2, choice,  1, pp1, pp2)
            else:
                oldhp = poke2.hp
                poke2.hp -=1+int(((poke1.cp+(poke1.attack))/((750+(poke2.defense))*1.5))*(moveinfo[poke1.moves[choice2]][0]))
                damage(oldhp, poke2.hp, poke2.maxhp, poke2.name)
                if poke2.hp < 1:
                    if iswin(pokelist1, pokelist2) == 1:
                        break
                    else:
                        while True:
                            betterprint('Choose a pokemon:\n')
                            for x in range(len(pokelist1)):
                                poke = pokelist1[x][0]
                                betterprint('{}. {}  {}/{}\n'.format(x+1, poke.name, poke.hp, poke.maxhp))
                            choice = input()
                            try:
                                value = int(choice)
                            except ValueError:
                                betterprint('Please put in a number!')
                            else:
                                choice = int(choice)
                                if choice < 1 or choice > len(pokelist1):
                                    betterprint('Please use a number that is in between 1 - {}'.format(len(poke1list)))
                                else:
                                    choice -= 1
                                    break
                        
                        weakness1, weakness2, poke1, poke2, num1, num2, num3, pokelist, pp1, pp2 = switch(pokelist1, pokelist2, weakness1, weakness2, poke1, poke2, num1, num2, choice,  1, pp1, pp2)
            betterprint(poke2.name+' used '+ poke2.moves[choice2-1]+'!')
        
        #if poke1 is faster
        elif moveinfo[poke1.moves[choice1]][3] < moveinfo[poke2.moves[choice2]][3]:
            data = attack(poke1, poke2, choice1, choice2, moveinfo, weakness1, weakness2)
            if data[0] == 1:
                poke2.hp = 0
                break
            elif data[1] == 2:
                poke1.hp = 0
                break
            else:
                poke1.hp = data[1]
                poke2.hp = data[2]
        #if poke2 is faster
        elif moveinfo[poke1.moves[choice1]][3] > moveinfo[poke2.moves[choice2]][3]:
            data = attack(poke2, poke1, choice2, choice1, moveinfo, weakness2, weakness1)
            if data[0] == 1:
                poke1.hp = 0
                break
            elif data[1] == 2:
                poke2.hp = 0
                break
            else:
                poke2.hp = data[1]
                poke1.hp = data[2]
        #if they tie
        else:
            if random.randint(0,1) == 1:
                data = attack(poke1, poke2, choice1, choice2, moveinfo, weakness1, weakness2)
                if data[0] == 1:
                    poke2.hp = 0
                    break
                elif data[1] == 2:
                    poke1.hp = 0
                    break
                else:
                    poke1.hp = data[1]
                    poke2.hp = data[2]
            else:
                data = attack(poke2, poke1, choice2, choice1, moveinfo, weakness2, weakness1)
                if data[0] == 1:
                    poke1.hp = 0
                    break
                elif data[1] == 2:
                    poke2.hp = 0
                    break
                else:
                    poke2.hp = data[1]
                    poke1.hp = data[2]


    if poke1.hp <= 0:
        betterprint(poke2.name+' fainted! '+poke1.name+' won the battle!')
        return poke2
    elif poke2.hp <= 0:
        betterprint(poke1.name+' fainted! '+poke2.name+' won the battle!')
        return poke1
    else:
        betterprint('Since one of your pokemon ran out of pp, this battle is deemed over and whoever ran out has lost.')

