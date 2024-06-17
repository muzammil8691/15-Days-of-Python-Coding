#Date: 16/6/2024
#Author: Muhammad Muzammil

#Write a program that cheks if a given number is positive, negative or zero.

def number_checker(number):
    if number == 0:
        print("You entered Zero")
    elif number > 0:
        print("You entered a Positive number")
    elif number < 0:
        print("You entered a Negative number")

number_checker(23)
number_checker(-89)
number_checker(0)
