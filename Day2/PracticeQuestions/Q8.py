#Date: 15/6/2024
#Author: Muhammad Muzammil

#implement a program that converts a given number of minutes into hpurs and minutes.\


def time_conversion(given_minutes):
    hours = given_minutes//60
    print(f"{hours} Hours")

    minutes = given_minutes%60
    print(f"{minutes} Minutes")


time_conversion(560)