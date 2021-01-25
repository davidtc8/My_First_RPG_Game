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

def branch_2():
    pass

def branch_1():
    clear_screen()
    typing("You wake up, you see that someone is knocking on your door")
    typing("You go and check to see who's knocking")
    typing(f"Ben: Hey {gen_character.getName()}, I just wanted to check if you're okay, I heard noises, are you okay?")
    decision_1 = int(input(typing("Yeah, I was snoring(1) / No, I'm not okay(2): ")))
    while decision_1 != 1 and decision_1 != 2:
        typing("You need to type '1' or '2', is it that hard?")
        decision_1 = int(input(typing("Yeah, I was snoring(1) / No, I'm not okay(2): ")))
    if decision_1 == 1:
        # decision if you were snoring
        typing("Ben: I'm pretty sure those were not snoring noises, but anyways, see you man, let me know if I there's anything I can help")
        typing(f"{gen_character.getName()}: (Thinking) Sure, fuck off")
    else:
        # decision if you're not okay
        typing("Ben: Do you want me to call the guards? The town is not safe lately")
        typing(f"{gen_character.getName()}: Nah I just feel dizzy man, want to come in and grab a bite?")
        time.sleep(3)
        typing("Ben: Sure, I'm starving")
        typing("As you let him enter, Ben is a talker, he starts immediately rumbling about some nonsense")
        typing("Ben: You know, the other day in the tavern, I heard a guy talking that all of this world was created for a single person")
        typing(f"{gen_character.getName()}: What do you mean for a single person? Lol")
        time.sleep(2)
        typing("Ben: Yes, all of this world is for a single person to grow and mature, that we're all the same")
        typing(f"{gen_character.getName()}: I don't follow, but its fine dude")
        typing(f"Ben: It's quite perturbing actually, for example, let's say for instance, that you die right now, \nhe was saying that after you die, you meet this guy that actually reincarnates you only to live another live\nAnd the only reason is for you to grow and mature")
        typing(f"{gen_character.getName()}: Oh, yeah that way we can all grow and mature living a lot of lives don't you think Ben")
        time.sleep(4)
        typing(f"Ben: No, {gen_character.getName()} is only you, there's no one else... is only for you to grow and mature...")
        typing(f"That's pretty deep Ben, you should stop going to that tavern dude, Lol")
        typing(f"Ben: You know I like to drink... seeing too many people dying lately just makes want to drink more")
        typing(f"{gen_character.getName()}: Yeah, I heard... that disease is killing everyone, isn't it?")
        time.sleep(2)
        typing(f"Ben: Yeah, I don't know what's happening actually, just seems like a year ago everything was fine...")
        print("\n")
        print("Prepare...")
        typing("As Ben was talking someone enters quickly and stabs him")
        
def chapter1():
    print(enemy_list["chapter1"])
    time.sleep(7)
    clear_screen()
    print(enemy_list["woods"])
    time.sleep(5)
    clear_screen()
    typing(f"{gen_character.getName()}, this is just the beginning, but remember, it's just you")
    time.sleep(3)
    clear_screen()
    typing("You wake up crying, you don't really know what is going on, you're dizzy, what do you do?")
    decision_1 = int(input(typing("You wake up(1) or do you want ot sleep a little bit more(2): ")))
    while decision_1 != 1 and decision_1 != 2:
        typing(f"{decision_1} is not either '1' or '2'... is it that hard to type '1' or '2' {gen_character.getName()}?")
        decision_1 = int(input(typing("You wake up(1) or do you want ot sleep a little bit more(2): ")))

    if decision_1 == 1:
        #follow the plot of the story with 1 when you're waking up
        time.sleep(2)
        branch_1()

    else:
        #follow the plot of the story with 2 if you slept a little bit more
        branch_2()




