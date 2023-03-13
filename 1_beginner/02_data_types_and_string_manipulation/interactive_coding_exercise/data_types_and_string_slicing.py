"""
Title: Printing Examples
Author: Chase Naquin
Date: March 13, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 2
Exercise: 21
Type: Interactive Coding Exercise

Description: Adding a multiple-digit number together with its own slices.
"""

# Get number input specifically as a string to allow for slicing.
digit = str(input("What number do you want to calc the sum of digit slices: "))


def slice_string_into_list(number_to_slice):
    tmp_slice_list = []
    # Appending each slice of the input string into the list.
    for number in range(0, (len(number_to_slice))):
        for char in number_to_slice[number]:
            tmp_slice_list.append(char)

    return tmp_slice_list


def calculate_total(slices):
    tmp_total = 0
    for char in slices:
        tmp_total += int(char)

    return tmp_total


slice_list = slice_string_into_list(digit)
total = calculate_total(slice_list)

print(f"Your selection of {digit}, broken down into {slice_list} results in the sum "
      f"total of slices: \"{total}\"!")
