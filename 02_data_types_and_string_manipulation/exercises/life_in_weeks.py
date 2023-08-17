"""
Title:          life_in_weeks
Author:         Chase Naquin
Date:           2023-03-14

Course:         100 Days of Code: The Complete Python Pro Bootcamp for 2023
Company:        App Brewery (On Udemy)
Author:         Angela Yu

Type:           Interactive Coding Exercise
Section:        Beginner
Day:            02
Exercise:       25

Description:    Calculating life in a variety of time measurements, both from birth and current time.

Competencies:   mathematical operators, datetime, converting dates, covernting times, printing datetime
"""


# Life in Years, Months, Weeks, Days, Hours, Minutes, Seconds
def life_time_breakdown():
    age = float(input("What is your age: "))
    life_expectancy = float(input("What age do you think you will live to: "))
    years_to_live = life_expectancy - age
    months_to_live = years_to_live * 12
    weeks_to_live = years_to_live * 52
    days_to_live = years_to_live * 365
    hours_to_live = days_to_live * 24
    minutes_to_live = hours_to_live * 60
    seconds_to_live = minutes_to_live * 60

    print(f"""
    Age: {age}
    Life Expectancy: {life_expectancy}

    Years Remaining (Total): {years_to_live}
    Months Remaining (Total): {months_to_live}
    Weeks Remaining (Total): {weeks_to_live}
    Days Remaining (Total): {days_to_live}
    Hours Remaining (Total): {hours_to_live}
    Minutes Remaining (Total): {minutes_to_live}
    Seconds Remaining (Total): {seconds_to_live}

    """)


# Lifetime countdown clock. How much lifetime do you have remaining in years, months, weeks, days,
# hours, minutes, seconds. (NOT DONE)
def lifetime_remaining():
    from datetime import datetime

    month, day, year = [int(item) for item in input('Enter a date formatted as MM/DD/YYYY: ').split('/')]
    days_old = datetime.now() - datetime(year, month, day, 0, 0, 0)
    print(days_old)
    # projected_life_expectancy = int(input("What is your projected life expectancy age: "))
    # remaining_days_to_live = days_old

# date_string = "201512"
# date_object = datetime.datetime.strptime(date_string, "%Y%m")
# print(date_object)
# print(date_object.year)


# life_time_breakdown()
lifetime_remaining()
