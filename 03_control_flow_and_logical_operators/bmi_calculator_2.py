"""
Title: Printing Examples
Author: Chase Naquin
Date: March 14, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 2
Exercise: 32
Type: Interactive Coding Exercise

Description: BMI Calculator 2.0 (with nested conditions).
"""

weight = float(input("What is your weight?: "))
height = float(input("what is your height?: "))


def bmi(weight_2, height_2):
    return weight_2 / (height_2 ** 2)


def range_category(bmi_number_):
    if 18.5 >= bmi_number_:
        return "underweight"
    elif 25 >= bmi_number_:
        return "normal weight"
    elif 30 >= bmi_number_:
        return "overweight"
    elif 35 >= bmi_number_:
        return "obese"
    else:
        return "clinically obese"


bmi_number = bmi(weight, height)
categorization = range_category(bmi_number)

print(f"Your bmi is {bmi_number} which is categorized as {categorization}")
