"""
Title: Printing Examples
Author: Chase Naquin
Date: March 14, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 2
Exercise: 33
Type: Interactive Coding Exercise

Description: Checking if an entered year is a leap year or not.

Leap Year Logic:
- On every year that is evenly divisible by 4
- except every year that is evenly divisible by 100
- unless the year is also evenly divisible by 400

Associated File:
leap_year_flow_chart.draw.io.xml
"""


def determine_leapyear(year_):
    if year_ % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("What year would you like to check: "))
is_leapyear = determine_leapyear(year)
print(f"Is {year} a leapyear: {is_leapyear}")
