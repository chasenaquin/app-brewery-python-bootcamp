"""
Title: Printing Examples
Author: Chase Naquin
Date: March 13, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 1
Exercise: 14
Type: Interactive Coding Exercise

Description: Switching 2 variable values.
"""


def switch_a_roo():
    a = input("a: ")
    b = input("b: ")

    # Must include a temporary variable to hold the value in the interim while switching values between primary two.
    c = a
    a = b
    b = c

    print(f"Swapped\na: {a}\nb: {b}")


switch_a_roo()
