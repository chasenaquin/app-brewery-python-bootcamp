"""
Title: Password Generator
Author: Chase Naquin
Date: March 22, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 3
Exercise: 44
Type: Daily Project

Description: Password Generator
"""

import random

letter_input = int(input("Letters: "))
numbers_input = int(input("Numbers: "))
special_characters_input = int(input("Special Characters: "))


def generate_password(letters, numbers, special_characters):
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    for index in range(0, letters):
        password_list.append(random.choice(list(letter_list)))
    for index in range(0, numbers):
        password_list.append(random.choice(list(number_list)))
    for index in range(0, special_characters):
        password_list.append(random.choice(list(symbol_list)))

    return password_list


passwordlist = generate_password(letter_input, numbers_input, special_characters_input)

password = ''
for i in range(0, len(passwordlist) - 1):
    index_letter = random.randint(0, len(passwordlist) - 1)
    password = password + passwordlist[index_letter]

print(password)


# Version 2
# TODO - Input only the number of characters you want the password to be.
# TODO - use argv to