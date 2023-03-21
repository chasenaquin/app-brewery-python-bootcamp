"""
Title: Printing Examples
Author: Chase Naquin
Date: March 18, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 3
Exercise: 38
Type: Daily Project

Description: A text interactive adventure game.
"""
# TODO Add auto generated numbers to the action choices to minimize typing

import random
from os import system
system('clear')
print('''

                                                                                                                                                               
         .8.          8 888888888o.    `8.`888b           ,8' 8 8888888888   b.             8 8888888 8888888888 8 8888      88 8 888888888o.   8 8888888888   
        .888.         8 8888    `^888.  `8.`888b         ,8'  8 8888         888o.          8       8 8888       8 8888      88 8 8888    `88.  8 8888         
       :88888.        8 8888        `88. `8.`888b       ,8'   8 8888         Y88888o.       8       8 8888       8 8888      88 8 8888     `88  8 8888         
      . `88888.       8 8888         `88  `8.`888b     ,8'    8 8888         .`Y888888o.    8       8 8888       8 8888      88 8 8888     ,88  8 8888         
     .8. `88888.      8 8888          88   `8.`888b   ,8'     8 888888888888 8o. `Y888888o. 8       8 8888       8 8888      88 8 8888.   ,88'  8 888888888888 
    .8`8. `88888.     8 8888          88    `8.`888b ,8'      8 8888         8`Y8o. `Y88888o8       8 8888       8 8888      88 8 888888888P'   8 8888         
   .8' `8. `88888.    8 8888         ,88     `8.`888b8'       8 8888         8   `Y8o. `Y8888       8 8888       8 8888      88 8 8888`8b       8 8888         
  .8'   `8. `88888.   8 8888        ,88'      `8.`888'        8 8888         8      `Y8o. `Y8       8 8888       ` 8888     ,8P 8 8888 `8b.     8 8888         
 .888888888. `88888.  8 8888    ,o88P'         `8.`8'         8 8888         8         `Y8o.`       8 8888         8888   ,d8P  8 8888   `8b.   8 8888         
.8'       `8. `88888. 8 888888888P'             `8.`          8 888888888888 8            `Yo       8 8888          `Y88888P'   8 8888     `88. 8 888888888888 
                                                                                                                                                               
 8 8888    d888888o.   8 8888                  .8.          b.             8 8 888888888o.                                                                     
 8 8888  .`8888:' `88. 8 8888                 .888.         888o.          8 8 8888    `^888.                                                                  
 8 8888  8.`8888.   Y8 8 8888                :88888.        Y88888o.       8 8 8888        `88.                                                                
 8 8888  `8.`8888.     8 8888               . `88888.       .`Y888888o.    8 8 8888         `88                                                                
 8 8888   `8.`8888.    8 8888              .8. `88888.      8o. `Y888888o. 8 8 8888          88                                                                
 8 8888    `8.`8888.   8 8888             .8`8. `88888.     8`Y8o. `Y88888o8 8 8888          88                                                                
 8 8888     `8.`8888.  8 8888            .8' `8. `88888.    8   `Y8o. `Y8888 8 8888         ,88                                                                
 8 8888 8b   `8.`8888. 8 8888           .8'   `8. `88888.   8      `Y8o. `Y8 8 8888        ,88'                                                                
 8 8888 `8b.  ;8.`8888 8 8888          .888888888. `88888.  8         `Y8o.` 8 8888    ,o88P'                                                                  
 8 8888  `Y8888P ,88P' 8 888888888888 .8'       `8. `88888. 8            `Yo 8 888888888P'                                                                     

                        ____________
                      .~      ,   . ~.
                     /                
                    /               ,  
                   |   .            '   |
                   |                    |
          XX       |  /~~\        /~~\  |       XX
        XX  X      | |  o  \    /  o  | |      X  XX
      XX     X     |  \____/    \____/  |     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     |           '  |     @%%;;@  X       X
X      X     @%%;;@   |. ` ; ; ; ;  ,|   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@@
                          
---------------===============+++++++++++++++===============---------------                  
               ---===[ BY: CHASE NAQUIN ]===---
---------------===============+++++++++++++++===============---------------
''')

action_dictionary = {
    "movement_actions": ["straight", "left", "right", "back"],
    "water_actions": ["swim", "walk around on shore", "cross on a fallen log", "cast levitation and float across"],
    "door_actions": ["open", "close", "walk past", "knock", "kick in the door"],
    "monster_actions": ["fight", "run away", "summon a golem to fight", "smoke bomb and vanish",
                        "Yell confident and violent threats to him"],
    "movement_game_over": ["Stepped into an endless pit. You died."],
    "water_game_over": ["You were eaten by a hoard of tiny piranha. You died."]
}


quest_scenario_dictionary = {
    "movement_quest_01": {
        "identifier": "movement_quest_01",
        "category": "movement",
        "description": "You approach a crossroad intersection. Which way will you venture?",
        "actions": action_dictionary["movement_actions"],
        "answer": "",
        "game_over": action_dictionary["movement_game_over"]
    },
    "water_quest_01": {
        "identifier": "water_quest_01",
        "category": "water",
        "description": "You emerge across an expansive dark lake. How will you advance?",
        "actions": action_dictionary["water_actions"],
        "answer": "",
        "game_over": action_dictionary["water_game_over"]
    }
}

quest_length = int(input("Quest length [1 - 10]: "))
quest_difficulty = int(input("Quest difficulty: [1 - 3]: "))


def generate_quest(quest_difficulty_, quest_scenarios):
    quest = random.choice(list(quest_scenarios.keys()))
#    actions = random.choices(list(quest_scenarios[quest]["actions"]), k=quest_difficulty_ + 1)
    actions = random.sample(list(quest_scenarios[quest]["actions"]), k=quest_difficulty_ + 1)
    answer = random.choice(list(actions))
    system('clear')
    print("Actions:")

    for action in actions:
        print(f" - {action}")

    choice = input(f"\n{quest_scenarios[quest]['description']}: ").lower()

    if choice == answer:
        system('clear')
        print(f"The correct option was {answer}...proceed forward. ")
        return True
    else:
        system('clear')
        print(f"The correct option was {answer}...")
        print(random.choice(list(quest_scenarios[quest]["game_over"])))
        return False


i = True
score = -1
while i is True: # OR WHILE GAME LENGTH < whatever was input.
    i = generate_quest(quest_difficulty, quest_scenario_dictionary)
    score += 1

print(f"Your Score: {score}")
