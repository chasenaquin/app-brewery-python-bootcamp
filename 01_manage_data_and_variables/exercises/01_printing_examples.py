"""
Title:          01_printing_examples
Author:         Chase Naquin
Date:           2023-03-13

Course:         100 Days of Code: The Complete Python Pro Bootcamp for 2023
Company:        App Brewery (On Udemy)
Author:         Angela Yu

Type:           Interactive Coding Exercise
Section:        Beginner
Day:            001
Exercise:       008

Description:    Listing examples of print statements and capabilities.
Competencies:   printing, concatenation, f-strings, and print formatting.
"""

# Standard print statement
print("The function is declared like this: ")

# Printing displaying quotes
print("print('what to print')")

# New lines using escape characters
print("Hello World!\nHello Word!")

# String concatenation
print("Hello" + " " + "Chase!")

# Printing escape characters
print("This is an escape character being printed: \\n")

# Printing utilizing f-strings
test_string = "TEST"
print(f"{test_string}")

# Printing utilizing types
# %d - integer
# %e - exponential
# %f - float
# %o - octal
# %x - hex

print("Test:  %s" % "This is a test string")

print("Test %s" % test_string)
