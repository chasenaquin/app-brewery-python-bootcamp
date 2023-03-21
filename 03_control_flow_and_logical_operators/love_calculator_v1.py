"""
Title: Printing Examples
Author: Chase Naquin
Date: March 20, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 3
Exercise: 37
Type: Interactive Coding Exercise

Description: "Love Calculator" compatibility of "True" and "Love" in 2 peoples names. Original Task
Take both people's names and check for the number of times the letters in the word TRUE occur.
Then check for the number of times the letters in the word LOVE occurs.
Combine the two to make a 2 digit number.
"""

true_list = ["t", "r", "u", "e"]
love_list = ["l", "o", "v", "e"]

name1 = input("First persons name: ").lower()
name2 = input("Second persons name: ").lower()
grouped = name1 + name2


def count_letters(name, list_):
    count = 0
    for item in list_:
        for letter in name:
            if letter == item:
                count += 1
    return count


true_value = count_letters(grouped, true_list)
love_value = count_letters(grouped, love_list)

print(f"{true_value}{love_value}")