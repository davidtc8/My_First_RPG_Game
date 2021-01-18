# importing modules
import random
import time
from pprint import pprint
from art1 import logo

# ***Clear the screen function***
import os

# import sleep to show output for some time period
from time import sleep

def clear_screen():
    """
    This function will clear the screen
    """
    sleep(2)
    os.system('cls')

# printing the logo
print(logo)
clear_screen()

# We're constructing a class name hero
# Hhealth = Hero Health
class Hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname

    # we're gonna get setters and getters
        # These are getters, where we can check the health or attack of the character
        def getHealth(self):
            return self.health
        def getAttack(self):
            return self.attack
        def getLuck(self):
            return self.luck
        def getRanged(self):
            return self.ranged
        def getDefence(self):
            return self.defence
        def getMagic(self):
            return self.magic
        def getName(self):
            return self.name

        # setters is what we can use to change a variable
        # for example if we want to set a new attack value
        def setHealth(self, newHealth):
            self.health = newHealth
        def setAttack(self, newAttack):
            self.attack = newAttack
        def setLuck(self, newLuck):
            self.luck = newLuck
        def setRanged(self, newRanged):
            self.ranged = newRanged
        def setDefence(self, newDefence):
            self.defence = newDefence
        def setMagic(self, newMagic):
            self.magic = newMagic

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
    print(f"Welcome to the game, Jimmy!")

    return (heroAttack, heroLuck, heroRanged, heroDefence, heroMagic, heroName)

# We're going to use class_data as a list, so 0 = heroAttack, 1 = heroLcuk and so on...
class_data = createClass()

character = Hero(100, class_data[0], class_data[1], class_data[2], class_data[3], class_data[4], class_data[5],)
pprint(vars(character))

