#Date: 20/6/2024
#Author: Muhammad Muzammil

#Given a list of numbers, find the sum and average using built-in functions.

def sum_fun(numbers):
    
    print(f"Sum of numbers is {sum(numbers)}") 
    
    print(f"Average of numbers is {sum(numbers)/len(numbers)}")

lst = [2,6,8,3]
sum_fun(lst)

