"""
Title: Printing Examples
Author: Chase Naquin
Date: March 13, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 3
Exercise: 37
Type: Interactive Coding Exercise

Description: "Love Calculator" compatibility of "True" and "Love" in 2 peoples names.
"""

# They want concatenated numbers, but this will an overly complicated script and a different calc method.
# Might be cheating on the exercise using this...but im changing how this is done.
# UGH- NOT SURE IF THIS EVEN WORKS AT THE MOMENT....

from collections import Counter

true_love_list = ["t", "r", "u", "e", "l", "o", "v", "e"]


def names_to_list():
    name = input("Name: ").lower()
    name1_list = []
    for position in range(0, len(name)):
        for letter in name[position]:
            name1_list.append(letter)
            if letter == " ":
                name1_list.remove(letter)
    # name1_list.sort()
    return name1_list


def compare_to_true_love(name_list, true_love_list_):
    # true_love_list_.sort()
    count = 0
    for i in true_love_list_:
        for x in name_list:
            if i == x:
                count += 1
    return count


def count_letter(string_, true_love_list_):
    count = 0
    for i in true_love_list_:
        print(f"{i}: {string_.count(i)}")



    #
    # for letter in range(0, len(true_love_list_)):
    #     print(f"Letter: {true_love_list_[letter]}")
    #     for letter2 in range(0, len(true_love_list_)):
    #         print(f"Letter2: {name1_list[letter2]}")
    #         if name1_list[letter] == true_love_list_[letter]:
    #             count += 1
    #         print(f"Count: {count}")
    # return count

# for each letter in true_love_list,
#     count +1
#     compare it to the entire name list
#         if match, count +1





# def count_letters(name_list, compare_string):
#     # Create a dictionary adding name_list and compare_string and counting the letters.
#     total_letter_comparison = Counter(name_list + compare_string)
#     # Removing the values from total_letter_comparison that are not shared (value of 1)
#     letter_dict = {key: val for key, val in total_letter_comparison.items() if val != 1}
#     return letter_dict
#
# def score(name_one_list, name_two_list):
#     for key in name_one_list:
#         print(f"{key} : {name_one_list[key]}")
#
#
# first_person_name = names_to_list()
# print(first_person_name)
# name1_letter_comparison = count_letters(first_person_name, true_love_list)
# print(name1_letter_comparison)
# score(name1_letter_comparison, true_love_list)

first_person = names_to_list()
second_person = names_to_list()

# first_person_score = compare_to_true_love(first_person, true_love_list)
# second_person_score = compare_to_true_love(second_person, true_love_list)

# print(first_person)
#
# print(first_person_score)
# print(second_person_score)

count_letter(first_person, true_love_list)