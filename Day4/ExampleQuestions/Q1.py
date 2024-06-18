#Date: 18/6/2024
#Author: Muhammad Muzammil

#Write a function to calculate the area of a circle given its radius

from math import pi, pow

def area_of_circle(radius):
    area = pi * pow(radius,2)
    print(area)


area_of_circle(radius=30)
