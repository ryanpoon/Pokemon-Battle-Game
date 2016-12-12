import random, sys, time
weakness = {'Normal':('Fighting', '???'),'Flying':('Ice', 'Electric', 'Rock', '???'), 'Water':('Electric', 'Grass', '???'), 'Fire':('Water', 'Rock', 'Ground', '???'), 'Grass':('Fire', 'Poison', 'Bug', 'Ice', 'Flying', '???'), 'Bug':('Fire', 'Flying', '???'), 'Ice':('Fire', 'Steel', 'Fighting', '???'), 'Rock':('Water', 'Grass', 'Ground', 'Fighting', 'Steel', '???'), 'Ground':('Water', 'Grass', 'Fighting', '???'), 'Electric':('Ground', 'Rock', '???'), 'Psychic':('Bug', 'Ghost', '???'), 'Fighting':('Psychic', 'Flying', '???'), 'Poison':('Psychic', 'Ground', '???'), 'Steel':('Ground', '???', 'Fire'), 'Bug':('Rock', '???'), 'Ice':('Rock', 'Steel', '???'), 'Ghost':('Ghost', '???'), 'Dragon':('Dragon', 'Ice', '???'), '???':('lol')}
def bars(hp):
    if hp < 1:
        return 0
    elif int(hp/10) == 0:
        return 1
    else:
        return int(hp/10)
def betterprint(string='', speed=.01, end='\n'):
    for i in range(len(string)-1):
        time.sleep(speed)
        print(string[i], end='')
    print(string[i+1], end = end)
def damage(hp, newhp, maxhp, name):
    dealt = hp-newhp
    bar1 = '*' * bars(hp)
    bar2 = '*' * bars(newhp)
    spaces1 = ' ' * (bars(maxhp)-bars(hp))
    spaces2 = ' ' * (bars(maxhp)-bars(newhp))
    betterprint('{}: {}/{} |{}{}|'.format(name, hp, maxhp, bar1, spaces1))
    print(' '*(len(name)+2), end='')
    betterprint('-{}'.format(dealt))
    betterprint('{}: {}/{} |{}{}|'.format(name, newhp, maxhp, bar2, spaces2))

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
def fight(poke1, poke2, moveinfo):
##    music = pyglet.resource.media('battlemusic.wav')
##    music.play()
##    pyglet.app.run()
    
    pp1 = [moveinfo[poke1.moves[0]][2], moveinfo[poke1.moves[1]][2]]
    pp2 = [moveinfo[poke2.moves[0]][2], moveinfo[poke2.moves[1]][2]]
    weakness1 = []
    weakness2 = []
    
    for x in poke1.poketype:
        for y in weakness[x]:
            weakness1.append(y)
    for x in poke2.poketype:
        for y in weakness[x]:
            weakness2.append(y)
    while poke1.hp>0 and poke2.hp>0:
        print('-------------------------------------------------------------')
        betterprint(poke1.name+'('+poke1.pokemon+'): '+str(poke1.hp)+'/'+str(poke1.maxhp)+' |'+('*'*bars(poke1.hp))+ (' '*(int(poke1.maxhp/10)-bars(poke1.hp))) +'|\n'+poke2.name+'('+poke2.pokemon+'): '+str(poke2.hp)+'/'+str(poke2.maxhp)+' |'+('*'*bars(poke2.hp))+ ((' '*(int(poke2.maxhp/10)-bars(poke2.hp))+ '|')))
        print('-------------------------------------------------------------')
        betterprint(poke1.name+''''s Moves:\n'''+'1. '+poke1.moves[0]+ ' PP: '+str(pp1[0])+'/'+str(moveinfo[poke1.moves[0]][2])+'\n2. '+poke1.moves[1]+ ' PP: '+str(pp1[1])+'/'+str(moveinfo[poke1.moves[1]][2]))
        while True:
            if pp1[0] == 0 and pp1[1] == 0:
                choice1 = None
                break
            betterprint('Which move do you want to use? Pick 1 or 2. ', end='')
            choice1 = input('')
            try:
                value = int(choice1)
            except ValueError:
                betterprint('Please put in a number!')
            else:
                choice1 = int(choice1)
                choice1-=1
                if choice1+1>2 or choice1+1<1:
                    betterprint('Please pick a number that is 1 or 2!')
                
                elif pp1[choice1] == 0:
                    betterprint('Out of PP!')
                else:
                    break
        print('\n'*50+'-------------------------------------------------------------\nIt is now player 2s turn.')
        betterprint(poke1.name+'('+poke1.pokemon+'): '+str(poke1.hp)+'/'+str(poke1.maxhp)+' |'+('*'*bars(poke1.hp))+ (' '*(int(poke1.maxhp/10)-bars(poke1.hp))) +'|\n'+poke2.name+'('+poke2.pokemon+'): '+str(poke2.hp)+'/'+str(poke2.maxhp)+' |'+('*'*bars(poke2.hp))+ ((' '*(int(poke2.maxhp/10)-bars(poke2.hp))+ '|')))
        print('-------------------------------------------------------------')
        betterprint(poke2.name+''''s Moves:\n'''+'1. '+poke2.moves[0]+ ' PP: '+str(pp2[0])+'/'+str(moveinfo[poke2.moves[0]][2])+'\n2. '+poke2.moves[1]+ ' PP: '+str(pp2[1])+'/'+str(moveinfo[poke2.moves[1]][2]))
        while True:
            if pp2[0] == 0 and pp2[1] == 0:
                choice2 = None
            betterprint('Which move do you want to use? Pick 1 or 2. ', end='')
            choice2 = input('')
            try:
                value = int(choice2)
            except ValueError:
                betterprint('Please put in a number!')
            else:
                choice2 = int(choice2)
                choice2 -= 1
                if choice2+1>2 or choice2+1<1:
                    betterprint('Please pick a number that is 1 or 2!')
                
                elif pp2[choice2] ==0:
                    betterprint('Out of PP!')
                else:
                    break
        betterprint('Press Enter to Continue', end = ' ')
        confirm = input('')
        pp1[choice1] -= 1
        pp2[choice2] -= 1
        print('\n'*50+'-------------------------------------------------------------\nTime for battle!')
        #if poke1 is faster
        if moveinfo[poke1.moves[choice1]][3] < moveinfo[poke2.moves[choice2]][3]:
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
        betterprint(poke1.name+' fainted! '+poke2.name+' won the battle!')
        return 2
    elif poke2.hp <= 0:
        betterprint(poke2.name+' fainted! '+poke1.name+' won the battle!')
        return 1
    else:
        betterprint('Since one of your pokemon ran out of pp, this battle is deemed over and whoever ran out has lost.')

