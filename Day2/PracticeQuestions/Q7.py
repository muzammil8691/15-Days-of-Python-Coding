#Date: 15/6/2024
#Author: Muhammad Muzammil

#Calculate the area and circumference of a circle given its radius.
#Area Formula = Pi x r square
#Circumference Formula = 2 x Pi x r

from math import pi, pow

def area_of_circle(radius):
    #This function calculates Area of circle #Docstring
    area = pi * pow(radius, 2)
    return area

def circumference_of_circle(radius):
    #This function calculates Circumference of circle #Docstring
    circumference = 2 * pi * radius
    return circumference


print(f"Area of circle is {area_of_circle(25)}")
print(f"Circumference of circle is {circumference_of_circle(25)}")