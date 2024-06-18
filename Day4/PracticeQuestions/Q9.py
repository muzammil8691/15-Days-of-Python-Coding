#Date: 18/6/2024
#Author: Muhammad Muzammil

#Implement a function to check if a given year is a leap year or not.

def leap_year(year):
    if year >= 1582:
        if year % 400 == 0:
            print("It's a Leap Year")
        elif year % 100 == 0:
            print("Not a Leap Year")
        elif year % 4 == 0:
            print("It's a Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("This Year doesn't comes under Gregorian Calendar")
    

leap_year(1900)
leap_year(2000)
leap_year(1498)
