"""
Title: Printing Examples
Author: Chase Naquin
Date: March 13, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 2
Exercise: 23
Type: Interactive Coding Exercise

Description: BMI Calculator enforcing data types.
"""


weight = float(input("What is your weight?: "))
height = float(input("what is your height?: "))


def bmi(weight_2, height_2):
    return weight_2 / (height_2 ** 2)


print(bmi(weight, height))
