#Date: 16/6/2024
#Author: Muhammad Muzammil

#Implement a program that prints the multiplication table of a given number.

def mul_table(number):
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")

mul_table(9)