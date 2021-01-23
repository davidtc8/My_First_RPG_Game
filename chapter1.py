#  importing modules
import math
import random
import time
from pprint import pprint
from art1 import logo, logo2, enemy_list
from hero_class import Hero
from enemy_class import Enemy, Boss, enemygen, enemy_attack
import os
from functions_for_the_game import level_generator, gen_character, createClass, typing, clear_screen

def chapter1():
    print(enemy_list["chapter1"])
    time.sleep(7)
    clear_screen()
    print(enemy_list["woods"])
    time.sleep(5)
    typing(f"{gen_character.getName()}, this is just the beginning, but remember, this is about you, there’s no one else…")
    time.sleep(5)
    typing("....")
    typing("Just you...")
    clear_screen()



