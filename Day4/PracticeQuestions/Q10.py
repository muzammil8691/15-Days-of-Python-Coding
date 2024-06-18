#Date: 18/6/2024
#Author: Muhammad Muzammil

#Create a function that takes a number as input and prints its multiplication table.


def mul_table(number):
    
    if number <= 0:
        print("Enter a Positive Number")
    else:
        for i in range(1,11):
            print(f"{number} x {i} = {number*i}")

number = int(input("Enter a number to print it's Multiplication table: "))
mul_table(number)
