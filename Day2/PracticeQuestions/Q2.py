#Date: 15/6/2024
#Author: Muhammad Muzammil

#Create a program that takes a temperature in Celsius and converts it to Kelvin.

def cel_to_kel(celsius):
    #this function converts temperature Celsius to Kelvin #DocString
    kelvin = celsius + 273.15
    return kelvin


print(f"{cel_to_kel(43)}K")
