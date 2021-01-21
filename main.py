# importing modules
import random
import time
from pprint import pprint
from art1 import logo, logo2
from hero_class import Hero
from enemy_class import Enemy, Boss, enemygen, enemy_attack
import os

# import sleep to show output for some time period
from time import sleep

# ***Clear the screen function***
def clear_screen():
    """
    This function will clear the screen
    """
    sleep(2)
    os.system('cls')

# printing the logo
print(logo)
clear_screen()

print(logo2)

# we're gonna ask the user a series of questions and the answers to those questions are gonna build our class
def createClass():
    print('Type "1" for first option, and "2" for the second option')
    a = int(input("Are you more strategic(1) or more of a warrior(2)?: "))
    while a != 1 and a != 2:
        print(f"{a} is not either '1' or '2'... invalid option")
        a = int(input("Are you more strategic(1) or more of a warrior(2)?: "))

    if a == 1:
        heroAttack = 50
        heroDefence = 100
    elif a == 2:
        heroAttack = 100
        heroDefence = 50

    # Determining the hero's luck!
    print("")
    time.sleep(.5)
    print("let's see how much luck you have")
    b = input("Press enter to roll a dice...")
    time.sleep(.5)
    print('Rolling dice...')
    heroLuck = random.randint(0,10)
    print(f"Your hero has {heroLuck} points out of 10")

    print("")
    print("Quite an interesting character....")
    # Determining the hero's magic!
    c = int(input("Are you more of a bow and arrow(1) or a magic user?(2): "))
    while c != 1 and c != 2:
        print(f"{c} is not either '1' or '2'... invalid option")
        c = int(input("Are you more of a bow and arrow(1) or a magic user(2)?: "))

    if c == 1:
        print("I thought you'd choose magic... Arrows are for assho***")
        time.sleep(2)
        print("But anyways, who am I to judge")
        heroRanged = 100
        heroMagic = 50
    elif c == 2:
        print("I thought you'd choose arrows... You only chose Magic because you don't want to fight...")
        time.sleep(2)
        print("But anyways, who am I to judge")
        heroRanged = 50
        heroMagic = 100

    print("")
    time.sleep(1)
    # Determining the hero's Name!
    heroName = input("Tell me your name, and please don't give me a boring one: ")
    time.sleep(2)
    print(f"Such a boring name... {heroName} is not a hero's name, I'll call you Jimmy!")
    heroName = 'Jimmy'
    time.sleep(2)
    clear_screen()
    print(f"Welcome to the game, Jimmy!")

    return (heroAttack, heroLuck, heroRanged, heroDefence, heroMagic, heroName)

# Some functions that will help us run our game smoother
def hit_chance(luck):
    hit = random.randint(0,4)
    if luck < hit:
        print("LOL, you missed")
        return False
    else:
        print("You hit the enemy!")
        return True

def is_dead(health):
    if health < 1:
        return True
    else:
        return False

def loot(luck, gen_character):
    lootChance = random.randint(0,4)
    if luck < lootChance:
        print("No loot found );")
    else:
        # I have 5 diff tables to look at, this tables are the txt files!
        table_number = random.randint(0,4)
        loot_table_list = ["items", 'ranged', 'defence', 'magic', 'attack']
        # through this new variable is going to randomly look up in any of the files
        item_type = loot_table_list[table_number]
        # opening the file
        with open(item_type + '.txt', 'r') as file:
            lines = file.readlines()

        print("The enemy dropped a....")
        item = random.randint(0, len(lines)-1)
        item_line = lines[item]
        split_item_line = item_line.split(',')
        item_name = split_item_line[0]
        value = int(split_item_line[1])
        print(item_name)

        if item_type == 'attack':
            # We programmed a lot of getters and setters so we can actually get them and edit them in here
            gen_character.setAttack(gen_character.getAttack() + value)
            print(f"Your new attack is {gen_character.getAttack()}")

        elif item_type == "ranged":
            gen_character.setRanged(gen_character.getRanged()+value)
            print("Your new Ranged Attack is...")
            print(gen_character.getRanged())

        elif item_type == "defence":
            # Hero.setDefence(Hero.getDefence()+value)
            gen_character.setDefence(gen_character.getDefence()+value)
            print("Your new Defence is...")
            print(gen_character.getDefence())

        elif item_type == "magic":
            gen_character.setMagic(gen_character.getMagic()+value)
            print("Your new Magic attack is...")
            print(gen_character.getMagic())

        else:
            if split_item_line[2] == 'luck':
                gen_character.setLuck(gen_character.getLuck() + value)
                print(f'Your new Luck is {gen_character.getLuck()}')

            elif split_item_line[2] == "health":
                gen_character.setHealth(gen_character.getHealth() + value)
                print(f"Your new Health is {gen_character.getHealth()}")

# We're going to use class_data as a list, so 0 = heroAttack, 1 = heroLcuk and so on...
class_data = createClass()
gen_character = Hero(Hhealth = 100, Hattack= class_data[0], Hluck= class_data[1], Hranged =  class_data[2], Hdefence = class_data[3], Hmagic = class_data[4], Hname = class_data[5],)
pprint(vars(gen_character))

# loot test!
loot(100, gen_character)
loot(100, gen_character)


print(f"Your hero stats are: {vars(gen_character)}")

# Setting everything for the enemies
levelBoss = True
enemy_1 = enemygen(levelBoss)
print(vars(enemy_1))
