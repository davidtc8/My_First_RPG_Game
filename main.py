# importing modules
import os
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