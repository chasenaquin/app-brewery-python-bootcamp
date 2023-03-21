"""
Title: Printing Examples
Author: Chase Naquin
Date: March 20, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 3
Exercise: 38
Type: Daily Project

Description: A text interactive adventure game. Actual task.
"""

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

tmp_decision1 = input("Left or Right?: ").lower()
decision1 = tmp_decision1[0]
if decision1 == "r":
    print("Fall into a hole. Game over")
elif decision1[0] == "l":
    tmp_decision2 = input("Swim or Wait?: ").lower()
    decision2 = tmp_decision2[0]
    if decision2[0] == "s":
        print("Attacked by trout. Game over.")
    elif decision2[0] == "w":
        tmp_decision3 = input("Which door - Blue or Red or Yellow?: ").lower()
        decision3 = tmp_decision3[0]
        if decision3[0] == "b":
            print("Eaten by beasts. Game over")
        elif decision3[0] == "r":
            print("Burned by a fire. Game over.")
        elif decision3[0] == "y":
            print("You Win!")
        else:
            print("That is not an option. You forfeit")
    else:
        print("That is not an option. You forfeit")
else:
    print("That is not an option. You forfeit")


