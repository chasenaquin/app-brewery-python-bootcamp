"""
Title: Printing Examples
Author: Chase Naquin
Date: March 17, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 3
Exercise: 35
Type: Interactive Coding Exercise

Description: Pizza Order using multiple if statement succession.
"""


def pizza_size():
    size_short = (input("Pizza Size: [S, M, L]: ").upper())
    if size_short == "S":
        cost = 15
        size = "Small"
    elif size_short == "M":
        cost = 20
        size = "Medium"
    elif size_short == "L":
        cost = 25
        size = "Large"
    else:
        return "Bad Selection"

    return size, cost


def pizza_toppings(pizza_size_):
    pepperoni = input("Would you like to add pepperoni? [Y, N]: ").upper()

    if pepperoni == "Y" and pizza_size_ == "Small":
        toppings_cost = 2
    elif pepperoni == "Y" and (pizza_size_ == "Medium" or pizza_size_ == "Large"):
        toppings_cost = 3
    elif pepperoni == "N":
        toppings_cost = 0
    else:
        return "Bad Selection"

    return pepperoni, toppings_cost


def pizza_extra_cheese():
    extra_cheese = input("Would you like to add extra cheese? [Y, N]: ").upper()

    if extra_cheese == "Y":
        cheese_cost = 1
    elif extra_cheese == "N":
        cheese_cost = 0
    else:
        return "Bad Selection"

    return extra_cheese, cheese_cost


pizza_size, pizza_size_cost = pizza_size()
pepperoni_choice, pizza_toppings_cost = pizza_toppings(pizza_size)
extra_cheese_choice, extra_cheese_cost = pizza_extra_cheese()


print(f"Your {pizza_size} pizza with ({pepperoni_choice}) 'pepperoni' and ({extra_cheese_choice}) "
      f"'Extra Cheese' comes out to: ${pizza_size_cost + pizza_toppings_cost + extra_cheese_cost}")

