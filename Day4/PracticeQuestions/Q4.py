#Date: 18/6/2024
#Author: Muhammad Muzammil

#Create a function to find the square of each element in a given list.

from math import pow

def square(lst):
    for number in lst:
        print(number ** 2, end=",")


lst = [2,3,4,5,6]
square(lst)