"""
Title: Printing Examples
Author: Chase Naquin
Date: March 13, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 1
Exercise: 16
Type: Daily Project

Description: Create a Band Name Generator.
"""


def band_name_generator():
    city = input("What's the name of the city you grew up in: ")
    pet_name = input("What's your pets name: ")

    print(f"Your band name could be: {city} {pet_name}")


band_name_generator()
