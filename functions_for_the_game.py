# importing modules
import math
import random
import time
from pprint import pprint
from art1 import logo, logo2, enemy_list
from hero_class import Hero
from enemy_class import Enemy, Boss, enemygen, enemy_attack, first_enemies
import os
import sys

# import sleep to show output for some time period
from time import sleep

# ***Clear the screen function***
def clear_screen():
    """
    This function will clear the screen
    """
    sleep(2)
    os.system('cls')

# function for making the illusion of typing on every print
def typing(message):
    #print("")
    print(message) # Eliminate this after testing...
    #for word in message:
        #time.sleep(random.choice([0.3, 0.11, 0.08, 0.07,   0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
        #sys.stdout.write(word)
        #sys.stdout.flush()
    #time.sleep(.1)
    return ""

# we're gonna ask the user a series of questions and the answers to those questions are gonna build our class
def createClass():
    global heroAttack, heroRanged, heroMagic, heroDefence, heroLuck
    typing('Type "1" for first option, and "2" for the second option')
    a = int(input(typing("Are you more strategic(1) or more of a warrior(2)?: ")))
    while a != 1 and a != 2:
        typing(f"{a} is not either '1' or '2'... invalid option\n")
        m1 = typing("Are you more strategic(1) or more of a warrior(2)?: \n")
        a = int(input(m1))

    if a == 1:
        # Strategic path
        heroAttack = 5
        heroDefence = 7
    elif a == 2:
        # Warrior path
        heroAttack = 10
        heroDefence = 15

    # Determining the hero's luck!
    time.sleep(.5)
    typing("Let's see how much luck you have")
    b = input(typing("Press enter to roll a dice..."))
    time.sleep(.5)
    typing('Rolling dice...')
    heroLuck = random.randint(3,10)
    typing(f"Your hero has {heroLuck} points out of 10")

    typing("Interesting...")
    # Determining the hero's magic!
    c = int(input(typing("Are you more of a bow and arrow(1) or a magic user?(2): ")))
    while c != 1 and c != 2:
        typing(f"{c} is not either '1' or '2'... invalid option")
        c = int(input(typing("Are you more of a bow and arrow(1) or a magic user(2)?: ")))

    if c == 1:
        # Archer Path
        typing("I thought you'd choose magic... Arrows are for assho***")
        time.sleep(2)
        typing("But anyways, who am I to judge")
        heroRanged = 15
        heroMagic = 10
    elif c == 2:
        typing("I thought you'd choose arrows... You only chose Magic because you don't want to fight...")
        time.sleep(2)
        typing("But anyways, who am I to judge")
        heroRanged = 10
        heroMagic = 15

    time.sleep(1)
    # Determining the hero's Name!
    heroName = input(typing("Tell me your name, and please don't give me a boring one: "))
    typing(f"You have created your character, {heroName}...")
    time.sleep(5)
    clear_screen()

    return (heroAttack, heroLuck, heroRanged, heroDefence, heroMagic, heroName)

# printing the logo
print(logo)
time.sleep(5)
clear_screen()

print(logo2)
# We're going to use class_data as a list, so 0 = heroAttack, 1 = heroLcuk and so on...
class_data = createClass()
gen_character = Hero(Hhealth = 100, Hattack= class_data[0], Hluck= class_data[1], Hranged = class_data[2], Hdefence = class_data[3], Hmagic = class_data[4], Hname = class_data[5])


# Some functions that will help us run our game smoother
def hit_chance(luck):
    hit = random.randint(0,4)
    if luck < hit:
        typing("LOL, you missed")
        return False
    else:
        typing("You hit the enemy!")
        return True

def is_dead(health):
    if health < 1:
        return True
    else:
        return False

def loot(luck, gen_character):
    lootChance = random.randint(0,4)
    if luck < lootChance:
        typing("No loot found );")
    else:
        # I have 5 diff tables to look at, this tables are the txt files!
        table_number = random.randint(0,4)
        loot_table_list = ["items", 'ranged', 'defence', 'magic', 'attack']
        # through this new variable is going to randomly look up in any of the files
        item_type = loot_table_list[table_number]
        # opening the file
        with open(item_type + '.txt', 'r') as file:
            lines = file.readlines()

        typing("The enemy dropped a....")
        item = random.randint(0, len(lines)-1)
        item_line = lines[item]
        split_item_line = item_line.split(',')
        item_name = split_item_line[0]
        value = int(split_item_line[1])
        typing(item_name)

        if item_type == 'attack':
            # We programmed a lot of getters and setters so we can actually get them and edit them in here
            gen_character.setAttack(gen_character.getAttack() + value)
            typing(f"Your new attack is {gen_character.getAttack()}")

        elif item_type == "ranged":
            gen_character.setRanged(gen_character.getRanged()+value)
            typing("Your new Ranged Attack is...")
            typing(gen_character.getRanged())

        elif item_type == "defence":
            # Hero.setDefence(Hero.getDefence()+value)
            gen_character.setDefence(gen_character.getDefence()+value)
            typing("Your new Defence is...")
            typing(gen_character.getDefence())

        elif item_type == "magic":
            gen_character.setMagic(gen_character.getMagic()+value)
            typing("Your new Magic attack is...")
            typing(gen_character.getMagic())

        else:
            if split_item_line[2] == 'luck':
                gen_character.setLuck(gen_character.getLuck() + value)
                typing(f'Your new Luck is {gen_character.getLuck()}')

            elif split_item_line[2] == "health":
                gen_character.setHealth(gen_character.getHealth() + value)
                typing(f"Your new Health is {gen_character.getHealth()}")

def game_over(enemyDead):
    """
    :param enemyDead:
    :return: this function will let us know when the game is over
    """
    if enemyDead == True:
        typing("You've killed your enemy")

    else:
        typing(f"You are out of health {class_data[5]}!")
        time.sleep(8)
        typing("It's a shame... Game Over")
        exit()

def battle(chapter, enemygen, gen_character):
    """
    :param enemygen:
    :param gen_character:
    :return: it will return the battle between the hero and the enemy
    """
    typing(pprint(vars(enemygen)))

    battle = True
    while battle:
        # if the chapter is 1
        if chapter == 1:
            typing(f"Choose your weapon {class_data[5]}!")
            typing("Bare Hands(1) \nSo  mething near you to throw(2)")
            typing(pprint(vars(first_enemies)))
            choice = int(input())
            while choice != 1 and choice != 2:
                typing(f"WTF... type correct dude..")
                typing("Bare Hands(1) \nSomething near you to throw(2)")
            if choice == 1:
                damage = gen_character.getAttack()
            if choice == 2:
                damage = gen_character.getAttack()
            typing("You are preparing for the attack")
            hit = hit_chance(gen_character.getLuck())
            if hit == True:
                enemygen.setHealth(enemygen.getHealth() - damage)
                typing("You've hit the enemy!")
                typing(f"The enemy health is {enemygen.getHealth()}")
            else:
                typing("Your attack missed!")

            enemy_is_dead = is_dead(enemygen.getHealth())

            if enemy_is_dead == False:
                # in this case as the enemy_attack is a negative value, we need to put the '+' sign because otherwise
                # it will give more life to our character when an enemy hits it.
                gen_character.setHealth(gen_character.getHealth() + enemy_attack(enemygen.getChance(), enemygen.getAttack(),enemygen.getName(), gen_character.getDefence()))

                # Checking if the enemy is dead
                character_is_dead = is_dead(gen_character.getHealth())

                if character_is_dead == True:
                    battle = False
                    return False

                else:
                    typing(f"You character remaining health is {gen_character.getHealth()}")

            # this else is when the enemy dies
            else:
                battle = False
                typing("You have defeated the enemy")

                return True

        else:
            # when there are other chapters
            typing(f"Choose your weapon {class_data[5]}!")
            typing("Sword Attack(1) \nRanged Attack(2) \nMagic Attack(3)")
            choice = int(input())
            while choice != 1 and choice != 2 and choice != 3:
                typing(f"WTF! A {enemygen.getName()} is trying to kill us and you're typing the wrong keys you donkey!")
                time.sleep(3)
                typing("Sword Attack(1) \nRanged Attack(2) \nMagic Attack(3) \n Choose your weapon: ")
                choice = int(input())
            if choice == 1:
                damage = gen_character.getAttack()
            elif choice == 2:
                damage = gen_character.getRanged()
            else:
                damage = gen_character.getMagic()

            typing("You are preparing for the attack")
            hit = hit_chance(gen_character.getLuck())

            if hit == True:
                enemygen.setHealth(enemygen.getHealth()- damage)
                typing("You've the enemy!")
                typing(f"The enemy health is {enemygen.getHealth()}")
            else:
                typing("Your attack missed!")

            enemy_is_dead = is_dead(enemygen.getHealth())

            if enemy_is_dead == False:
                # in this case as the enemy_attack is a negative value, we need to put the '+' sign because otherwise
                # it will give more life to our character when an enemy hits it.
                gen_character.setHealth(gen_character.getHealth() + enemy_attack(enemygen.getChance(), enemygen.getAttack(), enemygen.getName(), gen_character.getDefence()))

                # Checking if the enemy is dead

                character_is_dead = is_dead(gen_character.getHealth())

                if character_is_dead == True:
                    battle = False
                    return False

                else:
                    typing(f"You character remaining health is {gen_character.getHealth()}")

            # this else is when the enemy dies
            else:
                battle = False
                typing("You have defeated the enemy")
                typing("Did it drop any loot?")
                loot(gen_character.getLuck(), gen_character)

                return True

def level_generator(gen_character, level):
    # the function has 'level' as parameter, meaning that we put 1 as a parameter
    # math.ceil(level*5) its going to return the number of enemies * 5, so we're going to have 5 enemies lv 1
    max_number_of_enemies = math.ceil(level*5)
    for enemy in range(0, max_number_of_enemies):
        # chance of generating a boss while we're creating an enemy
        boss_chance = random.randint(1,10)
        if boss_chance > 7:
            levelBoss = True
        else:
            levelBoss = False
        character_dead = battle(enemygen(levelBoss), gen_character)
        game_over(character_dead)
