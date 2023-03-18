"""
Title: Printing Examples
Author: Chase Naquin
Date: March 13, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 1
Exercise: 12
Type: Interactive Coding Exercise

Description: Using the input function to prompt and assign to a variable.
"""


def name_length():
    name = input("What is your name? ")
    print(f"Hello {name}!")
    print(f"You have {len(name) - name.count(' ')} characters in your name!")


name_length()
