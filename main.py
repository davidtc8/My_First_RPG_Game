# importing modules
import math
import random
import time
from pprint import pprint
from art1 import logo, logo2
from hero_class import Hero
from enemy_class import Enemy, Boss, enemygen, enemy_attack
import os
from functions_for_the_game import level_generator, gen_character, createClass
from chapter1 import chapter1

# import sleep to show output for some time period
from time import sleep

# ***Clear the screen function***
def clear_screen():
    """
    This function will clear the screen
    """
    sleep(2)
    os.system('cls')

# the function that generates our character and his level
#def main():
    #print(f"Your hero stats are: {pprint(vars(gen_character))}")
    #level_generator(gen_character, 1)

# bringing the chapter 1 to the game
chapter1()

# loot test!
#loot(100, gen_character)
#loot(100, gen_character)

# Setting everything for the enemies
#levelBoss = False
#enemy_1 = enemygen(levelBoss)
#enemy_2 = enemygen(levelBoss)

#print(vars(enemy_1))

#testing

#who_died_battle1 = battle(enemy_1, gen_character)
#game_over(who_died_battle1)
#who_died_battle2 = battle(enemy_2, gen_character)
#game_over(who_died_battle2)