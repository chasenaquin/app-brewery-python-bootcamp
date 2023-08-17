"""
Title:          bmi_calculator
Author:         Chase Naquin
Date:           2023-03-14

Course:         100 Days of Code: The Complete Python Pro Bootcamp for 2023
Company:        App Brewery (On Udemy)
Author:         Angela Yu

Type:           Interactive Coding Exercise
Section:        Beginner
Day:            02
Exercise:       23

Description:    BMI Calculator (Basic)

Competencies:   Data types, mathematical operations
"""


weight = float(input("What is your weight?: "))
height = float(input("what is your height?: "))


def bmi(weight_2, height_2):
    return weight_2 / (height_2 ** 2)


print(bmi(weight, height))
