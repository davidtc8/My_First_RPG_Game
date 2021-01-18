# importing modules
import random
import time
from pprint import pprint

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
    a = int(input("Are you more strategic(1) or more of a warrior(2)?"))
    while a != 1 and a != 2:
        print(f"{a} is not either '1' or '2'... invalid option")
        a = int(input("Are you more strategic(1) or more of a warrior(2)?"))

    if a == 1:
        heroAttack = 50
        heroDefence = 100
    elif a == 2:
        heroAttack = 100
        heroDefence = 50

    # Determining the hero's luck!
    b = int(input("Press enter to roll a dice..."))
    time.sleep(.2)
    print('rolling dice...')
    heroLuck = random.randint(0,10)
