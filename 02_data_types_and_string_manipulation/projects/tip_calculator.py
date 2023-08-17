"""
Title:          tip_calculator
Author:         Chase Naquin
Date:           2023-03-14

Course:         100 Days of Code: The Complete Python Pro Bootcamp for 2023
Company:        App Brewery (On Udemy)
Author:         Angela Yu

Type:           Daily Project
Section:        Beginner
Day:            02
Exercise:       26

Description:    Calculating a total bill (base + tax + tip) and splitting between people.
Competencies:   function arguments
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
