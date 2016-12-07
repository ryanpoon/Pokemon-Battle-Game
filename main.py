from pikachu import Pikachu
from magikarp import Magikarp
from weedle import Weedle
from fighting import fight, betterprint
from raichu import Raichu
from gyarados import Gyarados
from pidgeotto import Pidgeotto
from pidgeot import Pidgeot
from pidgey import Pidgey
from kakuna import Kakuna
from beedrill import Beedrill
from lapras import Lapras
from rhyhorn import Rhyhorn
from rhydon import Rhydon
from squirtle import Squirtle
from wartortle import Wartortle
from blastoise import Blastoise
from bulbasaur import Bulbasaur
from ivysaur import Ivysaur
from venasaur import Venasaur
from charmander import Charmander
from charmeleon import Charmeleon
from charizard import Charizard
from eevee import Eevee
from jolteon import Jolteon
from flareon import Flareon
from vaporeon import Vaporeon
from moveinfo import moveinfo
from cubone import Cubone
from marowak import Marowak
from gastly import Gastly
from haunter import Haunter
from gengar import Gengar
from dratini import Dratini
from dragonair import Dragonair
from dragonite import Dragonite
from machop import Machop
from machoke import Machoke
from machamp import Machamp
from listofpokemon import listofpokemon
from zzzzzz import Aaaaaa
import random, time
betterprint("This is the Pokemon generator/fighter by Ryan Poon.\nCredit to the pokemon go database at http://www.pokemongodb.net for various pokemon \ninformation and move information.")
code = random.randint(10000, 999999)

def pokeinfo(name, poketype, description, moves, cp, height, weight, pokemon, hp, maxhp):
    global moveinfo
    return '-------------------------------------------------------------\nYour '+pokemon+' is named '+name+'.\n'+'Type(s): '+ ', '.join(poketype)+ '\n'+description+'\nCP: '+str(cp)+'\nHP: '+str(hp)+'/'+str(maxhp) +'\nMoves: '+moves[0]+' '+str(moveinfo[moves[0]][0])+'('+moveinfo[moves[0]][1]+ ') and '+ moves[1]+' '+str(moveinfo[moves[1]][0])+'('+moveinfo[moves[1]][1]+')\nHeight: '+str(height)+'m\nWeight: '+str(weight)+'kg'

def pokesimple(pokemon):
	return pokeinfo(pokemon.name, pokemon.poketype, pokemon.description, pokemon.moves, pokemon.cp, pokemon.height, pokemon.weight, pokemon.pokemon, pokemon.hp, pokemon.maxhp)

def custompokemon(lvl):
    global code
    betterprint('What pokemon do you want to make? ', end = '')
    custom = input('')
    betterprint('What will you name your pokemon? ', end = '')
    name = input('')
    if custom == 'pidgey' or custom == 'Pidgey':
        return Pidgey(name, lvl)
    elif custom == 'magikarp' or custom == 'Magikarp':
        return Magikarp(name, lvl)
    elif custom == 'pikachu' or custom == 'Pikachu':
        return Pikachu(name, lvl)
    elif custom == 'weedle' or custom == 'Weedle':
        return Weedle(name, lvl)
    elif custom == 'raichu' or custom == 'Raichu':
        return Raichu(name, level = lvl)
    elif custom == 'gyarados' or custom == 'Gyarados':
        return Gyarados(name, level = lvl)
    elif custom == 'pidgeotto' or custom == 'Pidgeotto':
        return Pidgeotto(name, level = lvl)
    elif custom == 'pidgeot' or custom == 'Pidgeot':
        return Pidgeot(name, level = lvl)
    elif custom == 'kakuna' or custom == 'Kakuna':
        return Kakuna(name, level = lvl)
    elif custom == 'beedrill' or custom == 'Beedrill':
        return Beedrill(name, level = lvl)
    elif custom == 'lapras' or custom == 'Lapras':
        return Lapras(name, level = lvl)
    elif custom == 'rhyhorn' or custom == 'Rhyhorn':
        return Rhyhorn(name, level=lvl)
    elif custom == 'rhydon' or custom == 'Rhydon':
        return Rhydon(name, level = lvl)
    elif custom == 'squirtle' or custom == 'Squirtle':
        return Squirtle(name, level = lvl)
    elif custom == 'wartortle' or custom == 'Wartortle':
        return Wartortle(name, level = lvl)
    elif custom == 'blastoise' or custom == 'Blastoise':
        return Blastoise(name, level = lvl)
    elif custom == 'bulbasaur' or custom == 'Bulbasaur':
        return Bulbasaur(name, level = lvl)
    elif custom == 'ivysaur' or custom == 'Ivysaur':
        return Ivysaur(name, level = lvl)
    elif custom == 'venasaur' or custom == 'Venasaur':
        return Venasaur(name, level = lvl)
    elif custom == 'charmander' or custom == 'Charmander':
        return Charmander(name, level = lvl)
    elif custom == 'charmeleon' or custom == 'Charmeleon':
        return Charmeleon(name, level = lvl)
    elif custom == 'charizard' or custom == 'Charizard':
        return Charizard(name, level = lvl)
    elif custom == 'vaporeon' or custom == 'Vaporeon':
        return Vaporeon(name, level = lvl)
    elif custom == 'flareon' or custom == 'Flareon:':
        return Flareon(name, level = lvl)
    elif custom == 'jolteon' or custom == 'Jolteon':
        return Jolteon(name, level = lvl)
    elif custom == 'cubone' or custom == 'Cubone':
        return Cubone(name, level = lvl)
    elif custom == 'marowak' or custom == 'Marowak':
        return Marowak(name, level = lvl)
    elif custom == 'gastly' or custom == 'Gastly':
        return Gastly(name, level = lvl)
    elif custom == 'haunter' or custom == 'Haunter':
        return Haunter(name, level = lvl)
    elif custom == 'gengar' or custom == 'Gengar':
        return Gengar(name, level = lvl)
    elif custom == 'dratini' or custom == 'Dratini':
        return Dratini(name, level = lvl)
    elif custom == 'dragonair' or custom == 'Dragonair':
        return Dragonair(name, level = lvl)
    elif custom == 'dragonite' or custom == 'Dragonite':
        return Dragonite(name, level = lvl)
    elif custom == 'machop' or custom == 'Machop':
        return Machop(name, level = lvl)
    elif custom == 'machoke' or custom == 'Machoke':
        return Machoke(name, level = lvl)
    elif custom == 'machamp' or custom == 'Machamp':
        return Machamp(name, level = lvl)
    elif custom == str(code):
        return Aaaaaa('???', level = lvl)
    else:
        betterprint("We don't have that pokemon yet. Here. Have a pidgey.")
        return Pidgey(name, level = lvl)
def makepokemon(lvl):
    while True:
        betterprint('How many pokemon? ', end='')
        thingy = input('')
        try:
            value = int(thingy)
        except ValueError:
            betterprint('Please put in a number!')
        else:
            break
    for x in range(int(thingy)):
        print(pokesimple(custompokemon(lvl)))
    return None
def fightpokemon(lvl):
    global moveinfo
    betterprint('Player One Choose Your Pokemon')
    p1 = custompokemon(lvl)
    print(pokesimple(p1))
    betterprint('Press Enter to Continue', end=' ')
    confirm = input('')
    print('\n'*50+'-------------------------------------------------------------')
    betterprint('Player Two Choose Your Pokemon')
    p2 = custompokemon(lvl)
    print(pokesimple(p2))
    betterprint('Press Enter to Continue', end = ' ')
    confirm = input('')
    print('\n'*50)
    if fight(p1, p2, moveinfo) == 1:
        return 1
    else:
        return 2
    print('-------------------------------------------------------------')
def championbattle(lvl):
    player1wins = 0
    player2wins = 0
    while True:
        print('-------------------------------------------------------------')
        betterprint("Player 1's Wins: {}/3".format(player1wins))
        betterprint("Player 2's Wins: {}/3".format(player2wins))
        print('-------------------------------------------------------------')
        if player1wins == 2 or player2wins ==2:
            betterprint('Matchpoint!')
        betterprint('Press Enter to Continue')
        confirm = input('')
        winner = fightpokemon(lvl)
        if winner == 1:
            player1wins +=1
        else:
            player2wins +=1
        if player1wins == 3:
            betterprint('Player 1 wins!')
            break
        elif player2wins == 3:
            betterprint('Player 2 wins!')
            break
def rockpapereevee(lvl):
    betterprint('What will you name your Eevee(that will later be evolved)? ', end = ' ')
    name = str(input(''))
    p1 = Eevee(name, level=lvl)
    p1 = p1.evolve(lvl)
    print(pokesimple(p1))
    betterprint('Press Enter to Continue', end=' ')
    confirm = input('')
    print('\n' * 50)
    betterprint('What will you name your Eevee(that will later be evolved)? ', end = ' ')
    name = str(input(''))
    p2 = Eevee(name, level = lvl)
    p2 = p2.evolve(lvl)
    print(pokesimple(p2))
    betterprint('Press Enter to Continue', end = ' ')
    confirm = input('')
    fight(p1, p2, moveinfo)
betterprint('Press Enter to Continue', end=' ')
confirm = input('')
while True:
    betterprint('What level are you? 1(Noob) - 40(Pokemon Master): ', end = '')
    lvl = input('')
    try:
        value = int(lvl)
    except ValueError:
        betterprint('Please put in a number!')
    else:
        lvl = int(lvl)
        if lvl>40 or lvl<1:
            betterprint('No levels above 40 or below 1!')
        else:
            break
if lvl<10:
    betterprint("Looks like you are pretty new to this! Let me give you a rundown.\nHello there! Welcome to the world of Pokemon! My name is Oak!\nPeople call me the Pokemon Prof! This world\nis inhabited by creatures called Pokemon! For some people,\nPokemon are pets. Others use them for fights...\nYour very own Pokemon adventure is about to unfold! A world of dreams and adventures with Pokemon awaits! Lets go!", .02)
pokemon = []
print('-------------------------------------------------------------')
while True:
    betterprint('Which option do you want to use?\n  1. Make Pokemon!\n  2. Fight Pokemon!\n  3. Rock Paper Eevee\n  4. Change Level\n  5. Champion Battle\n  6. List of Pokemon\n  7. Exit')
    option = input('')
    try:
        value = int(option)
    except ValueError:
        betterprint('Please put in a number!')
    else:
        option = int(option)
        if option == 1:
            makepokemon(lvl)
        elif option == 2:
            fightpokemon(lvl)
        elif option == 3:
            rockpapereevee(lvl)
        elif option == 4:
            betterprint('What do you want your new level to be?')
            lvl = input('')
            try:
                value = int(lvl)
            except ValueError:
                betterprint('Please put in a number!')
            else:
                lvl = int(lvl)
                if lvl>40 or lvl<1:
                    betterprint('No levels above 40 or below 1!')
        elif option == 5:
            championbattle(lvl)
        elif option == 6:
            betterprint(listofpokemon, 0.001)
        elif option == 7:
            break
        elif option == 151:
            print(code)
        else:
            betterprint('That is not a valid answer')
betterprint('Thanks for Playing!')
