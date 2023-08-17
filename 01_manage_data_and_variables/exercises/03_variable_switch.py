"""
Title:          variable_switch
Author:         Chase Naquin
Date:           2023-03-13

Course:         100 Days of Code: The Complete Python Pro Bootcamp for 2023
Company:        App Brewery (On Udemy)
Author:         Angela Yu

Type:           Interactive Coding Exercise
Section:        Beginner
Day:            01
Exercise:       14

Description:    Switch the values of 2 variables. Start to use programatic logic.

Competencies:   Beginner programtic problem solving and logic and variables.
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
