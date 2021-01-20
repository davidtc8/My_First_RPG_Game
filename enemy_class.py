import random

# We're constructing a enemy class
class Enemy:
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename):
        # attributes for the enemy class
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance
        self.name = Ename

    # getters for the enemy class
    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getSpecial(self):
        return self.special

    def getChance(self):
        return self.chance

    def getName(self):
        return self.name

    # setters for the enemy class
    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setSpecial(self, newSpecial):
        self.special = newSpecial

    def setChance(self, newChance):
        self.chance = newChance

    def setName(self, newName):
        self.name = newName

    # we're going to make an inherit method
    # the parent class will be the enemy method and the boss will be the child class

class Boss(Enemy):
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename, EsuperMove):
        # in order to actually inherit the Enemy class we need to use the super method
        super().__init__(Ehealth, Eattack, Especial, Echance, Ename)
        self.superMove = EsuperMove

    # getter for SuperMove
    def getSuper(self):
        return self.superMove

    # setter for SuperMove
    def setSuper(self, newSuperMove):
        self.superMove = newSuperMove

# If I want to create a last boss or something I can just create an inheritance of Boss with the super method

# creating a function to create enemies
def enemygen(levelBoss):
    temp = []
    with open('adjective.txt', 'r') as file:
        lines = file.readlines()
        # as we want to choose a random adjective, our adjective is going to be between
        # the first adjective (0) and the lenght of the file -1 because of how Python operates the numbers
        # we're putting the [:-1] to eliminate from the text the '/n' that appears in each letter
        adjective = lines[random.randint(0, len(lines)-1)][:-1]
    with open('animal.txt', 'r') as file2:
        lines2 = file2.readlines()
        animal = lines2[random.randint(0, len(lines)-1)][:-1]

    if levelBoss == False:
        health = random.randint(50, 100)
        attack = random.randint(1,10)
        special = random.randint(10,20)
        chance = random.randint(1,10)

        # In here we're saying: call the class Enemy and give those attributes
        return Enemy(health, attack, special, chance, adjective + " " + animal)

    else:
        health = random.randint(200, 250)
        attack = random.randint(20, 40)
        special = random.randint(50, 60)
        chance = random.randint(1, 8)
        superMove = random.randint(100,200)

        # Return the Boss object and give it those attributes
        return Boss(health, attack, special, chance, adjective + " " + animal, superMove)