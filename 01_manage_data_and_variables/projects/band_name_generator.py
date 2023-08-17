"""
Title:          band_name_generator
Author:         Chase Naquin
Date:           2023-03-13

Course:         100 Days of Code: The Complete Python Pro Bootcamp for 2023
Company:        App Brewery (On Udemy)
Author:         Angela Yu

Type:           Daily Project
Section:        Beginner
Day:            01
Exercise:       16

Description:    Create a name generator using 2 user inputs.

Competencies:   input functions, user input, variables, f-strings.
"""



def band_name_generator():
    city = input("What's the name of the city you grew up in: ")
    pet_name = input("What's your pets name: ")

    print(f"Your band name could be: {city} {pet_name}")


band_name_generator()
