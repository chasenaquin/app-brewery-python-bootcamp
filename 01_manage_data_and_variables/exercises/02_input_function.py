"""
Title:          input_functions
Author:         Chase Naquin
Date:           2023-03-14

Course:         100 Days of Code: The Complete Python Pro Bootcamp for 2023
Company:        App Brewery (On Udemy)
Author:         Angela Yu

Type:           Interactive Coding Exercise
Section:        Beginner
Day:            01
Exercise:       12

Description:    User input calculator for lenght of name.
Competencies:   input functions, f-strings.
"""



def name_length():
    name = input("What is your name? ")
    print(f"Hello {name}!")
    print(f"You have {len(name) - name.count(' ')} characters in your name!")


name_length()
