"""
Title: Printing Examples
Author: Chase Naquin
Date: March 14, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 3
Exercise: 30
Type: Interactive Coding Exercise

Description: Check if a number is odd or even.
"""


def check_if_even(number_):
    if number_ % 2 == 0:
        return True
    else:
        return False


number = int(input("Number to test: "))

is_even = check_if_even(number)
print(f"Is {number} an even number?: {is_even}")
