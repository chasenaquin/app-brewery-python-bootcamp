"""
Title: Printing Examples
Author: Chase Naquin
Date: March 14, 2023

Course: Udemy: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
Section: 2
Exercise: 26
Type: Daily Project

Description: Tip Calculator.
"""


def tip_calculator(bill_, tip_, people_):
    total_bill_per_person = (bill_ + (bill_ * (tip_ / 100))) / people_
    return total_bill_per_person


print("WELCOME TO THE TIP CALCULATOR")
bill = float(input("What was the total bill: $"))
tip = float(input("Tip percent: %"))
people = int(input("How many people to split the bill between: #"))

dutch_bill = tip_calculator(bill, tip, people)

print(f"Each person should pay: ${round(dutch_bill, 2):.2f}")
