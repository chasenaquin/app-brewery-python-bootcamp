"""
Title:          data_types_and_string_slicing
Author:         Chase Naquin
Date:           2023-03-14

Course:         100 Days of Code: The Complete Python Pro Bootcamp for 2023
Company:        App Brewery (On Udemy)
Author:         Angela Yu

Type:           Interactive Coding Exercise
Section:        Beginner
Day:            02
Exercise:       21

Description:    Adding the slices of a  multi-digit number together.

Competencies:   data types, string-slicing, range() function, lists, for loop, len() function, list operations, counter
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
