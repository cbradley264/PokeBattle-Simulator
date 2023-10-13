import time
import random
import os

def poke_select():
    os.system("cls")
    pokemon_options = ['Gengar', 'Gardevoir', 'Rayquaza', 'Garchomp', 'Sylveon', 'Umbreon', 'Charizard', 'Mimikyu', 'Lucario', 'Greninja']
    isTrue = True #used in error checking to make sure all inputs from user are valid
    thing = "=" * 140 #so it looks nice
    typingprint(thing)
    typingprint(f"\nWelcome to the Pokemon Battle simulator, where you can choose from 10 popular pokemon and battle a computer- controlled opponent.")
    name = typeInput("\nFirst, tell us your name: ")
    typingprint(f"\nHi {name}, welcome to the game. You will have the opportunity to choose from the following 10 pokemon.\n")
    print(pokemon_options)
    time.sleep(3) #give the user time to read
    while isTrue:
        typingprint("\nPut a number 1 - 10 to pick the corresponding pokemon.")
        typingprint("\nYour opponent will choose randomly from the other leftover Pokemon. Choose wisely!\n")
        time.sleep(2)
        poke_number = typeInput("\nWhich number will you choose? ")
        if(poke_number.isdigit() and int(poke_number) in range (1, 11)): #adjusted so that it can be a number 1- 10 instead of 0-9 (I feel like it's easier that way)
            isTrue = False #since inputs are valid, to ensure loop ends
            poke_number = int(poke_number)
            typingprint(f"\nFantastic, your pokemon of choice is {pokemon_options[poke_number - 1]}.")
            pokemon = pokemon_options[poke_number - 1]
            pokemon_options.remove(pokemon) #takes out user's pokemon so opponent can select from others
            time.sleep(2)
        else:
            print("Sorry, it looks like you picked a number outside of the range or didn't pick a number at all. \nPlease try again.\n")
            time.sleep(2) 
            print(f"{pokemon_options}\n")
    enemy_pokemon = pokemon_options[random.randint(0, 8)] #random number out of the 9 remaining for opponent
    typingprint(f"\nYour opponent chose {enemy_pokemon} to battle. May the best trainer win!")
    time.sleep(2)
    return pokemon, enemy_pokemon, name

def move(pokemon, j, k): #change movesets to a dictionary where each key is the name of the pokemon for easier access
#I like having this complex nested list in list in dictionary as a function, because I feel like it makes it easier to access specific elements
#format is- "pokemon name": [["move 1 name", move 1 damage], ...., ["move 4 name", move 4 damage]]
    movesets = {"Gengar": [["Lick", 8], ["Shadow Ball", 23], ["Hex", 18], ["Sludge Blast", 20]], #gengar
                "Gardevoir": [["Dazzling Gleam", 1], ["Moonblast", 19], ["Dream Eater", 30], ["Night Shade", 25]], #gardevoir
                "Rayquaza": [["Air Slash", 25], ["Aerial Ace", 15], ["Crunch", 20], ["Hyper Beam", 50]], #rayquaza
                "Garchomp": [["Dragon Claw", 12], ["Slash", 15], ["Tackle", 5], ["Dragon Rush", 25]], #garchomp
                "Sylveon": [["Draining Kiss", 12], ["Moonblast", 15], ["Covet", 1], ["Last Resort", 99]], #Sylveon
                "Umbreon": [["Swift", 12], ["Assurance", 22], ["Dark Pulse", 19], ["Last Resort", 8]], #umbreon
                "Charizard": [["Dragon Claw", 12], ["Fire Spin", 15], ["Slash", 20], ["Flare Blitz", 35]], #charizard
                "Mimikyu": [["Wood Hammer", 10], ["Shadow Claw", 18], ["Shadow Sneak", 20], ["Play Rough", 15]], #mimikyu
                "Lucario": [["Extreme Speed", 12,], ["Meteor Mash", 15], ["Bone Rush", 30], ["Close Combat", 18]], #lucario
                "Greninja": [["Aerial Ace", 18], ["Extrasensory", 25], ["Water Pulse", 15], ["Hydro Pump", 20]]} #greninja
    return movesets[pokemon][j][k]

def battle(pokemon, enemy_pokemon, name):
    your_hp = 100 #both pokemon will have same hitpoints for simplicity
    enemy_hp = 100
    opponent_turn = True #variable that checks if the opponent has taken their turn yet in current loop
    os.system("cls")

    typingprint("Welcome to the battlefield, trainers!")
    typingprint("\nDue to the fact that we made you select your pokemon without knowing anything about them besides their names, ")
    typingprint("\neach pokemon will have the same base stats, and a coin will be flipped to decide who goes first.")
    time.sleep(2)
    die = random.randint(1, 2)

    if die == 1:
       typingprint(f"\nIt looks like you will be going first, {name}!")
    else:
       typingprint("\nYour opponent will be going first.")
       opponent_turn = False
    
    while your_hp > 0 and enemy_hp > 0: #while both pokemon are alive
        time.sleep(2)
        if opponent_turn: #opponent has "already taken their turn"
            typingprint("\nIt's your turn!")
            typingprint("\nUse 1 through 4 to select the corresponding move:\n")
            print("="*70) #display formatted so that shows moves and damage to help user decide what move to use
            print("\n\t(1){:<30}(2){:<40}\nDamage:\t{:^10}{:>30}".format(move(pokemon, 0, 0), move(pokemon, 1, 0), move(pokemon, 0, 1), move(pokemon, 1, 1)))
            print("\n\t(3){:<30}(4){:<40}\nDamage:\t{:^10}{:>30}\n".format(move(pokemon, 2, 0), move(pokemon, 3, 0), move(pokemon, 2, 1), move(pokemon, 3, 1)))
            print("="*70)
            pointy = input()
            opponent_turn = False
            opponent_damage = 0
            if (pointy.isdigit() and int(pointy) in range (1, 5)):
                pointy = int(pointy)
                your_damage = move(pokemon, pointy - 1, 1)
                time.sleep(1)
                talktome = "\nYour {} used {}, and it hit for {}!\n".format(pokemon, move(pokemon, pointy - 1, 0), your_damage)
                typingprint(talktome) #since this function only prints strings and not variables, use f string and put that in
            else:
                your_damage = 0 #since the user incorrectly inputted something that wasnt a move, should skip turn
                typingprint("Unfortunately, you didn't correctly input a move. Therefore, your pokemon didn't have time to respond, and you lost your turn. \nNext time, make sure you input only a number 1 through 4.")
        else:
            die = random.randint(0, 3) #opponent gets random move selected for ease
            opponent_damage = move(enemy_pokemon, die, 1)
            your_damage = 0
            opponent_turn = True #since opponent just took turn
            talktome = "\nYour opponent's {} used {} and it hit for {}!\n".format(enemy_pokemon, move(enemy_pokemon, die, 0), opponent_damage)
            typingprint(talktome)
        time.sleep(1)
        your_hp = your_hp - opponent_damage #I figured it was best to always do both and on opponent turn, your_damage is 0, and vice versa
        enemy_hp = enemy_hp - your_damage
        if your_hp < 0: #this is just for display purposes, in the following print statement, so that health doesn't ever go below 0 
            your_hp = 0
        elif enemy_hp < 0:
            enemy_hp = 0
        talktome = "\nNow, your {}'s new hp is {}, and your opponents {}'s hp is {}.\n".format(pokemon, your_hp, enemy_pokemon, enemy_hp)
        typingprint(talktome)
    if(enemy_hp <= 0 and your_hp > 0): #this is the set of messages that should display if you win the game
        thing = "=" * 100
        typingprint(thing)
        time.sleep(1)
        os.system("cls")#clears the terminal, just because I think it looks nice
        thing = "=" * 100
        typingprint(thing)
        talktome = "\nYour opponent's {} has fainted.\n\n".format(enemy_pokemon)
        typingprint(talktome)
        talktome = "Congratulations, {}! You and your {} have successfully won today's battle!\n".format(name, pokemon)
        typingprint(talktome)
        typingprint("\nPlease come back and play again sometime.")
    elif(enemy_hp > 0 and your_hp <= 0): #if you lose the game (it should be pretty easy to avoid losing)
        thing = "=" * 100
        typingprint(thing)
        time.sleep(1)
        os.system("cls")
        thing = "=" * 100
        typingprint(thing)
        talktome = "\nYour {} has fainted.\n".format(pokemon)
        typingprint(talktome)
        time.sleep(1)
        typingprint("Unfortunately, you have lost this battle, and your pokemon must recover. \nHowever, you're welcome back anytime to try again!")

def typingprint(text): #function that creates the scrolling text effect that I think really adds to user experience
  for character in text:
    print(character, end = "", flush= True)
    time.sleep(0.01) #the speed the characters appear- for testing purposes, it's pretty fast but it would be easy enough to slow down
#however, constraint is that it only takes in strings (it would've been pretty easy to do print f but I was stupid and forgot)
#as a result, you have to make a separate string with the variable already in it and then print that, which is what "talktome" is
def typeInput(text): #acts exactly like the print function above except also takes input and returns it
  for character in text:
    print(character, end = "", flush= True)
    time.sleep(0.01)
  value = input()
  return value

def main():
    chosen_pokemon, enemy_pokemon, name = poke_select() 
    battle(chosen_pokemon, enemy_pokemon, name)

if __name__ == '__main__':
    main()