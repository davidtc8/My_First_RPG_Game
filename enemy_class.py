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
