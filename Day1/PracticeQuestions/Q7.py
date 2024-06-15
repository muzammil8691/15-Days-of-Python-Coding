#Date: 14/6/2024
#Author: Muhammad Muzammil

#Write a program that converts a given number of days into years, weeks and days.


def conversion(days):
    years = days//365
    print(f"Years : {years}")

    weeks = (days%365)//7
    print(f"Weeks : {weeks}")

    days = days - ((years*365) + (weeks*7))
    print(f"Days : {days}")


conversion(373)
conversion(364)
conversion(365)
