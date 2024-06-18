#Date: 18/6/2024
#Author: Muhammad Muzammil

#Implement a function that returns the factorial of a given number by using recursion.

def recursion_factorial(number):
    #Factorial using recursion(calling function in itself)
    if number == 0 or number == 1:
        return 1 
    else:
        return number * recursion_factorial(number-1)


print(recursion_factorial(5))
print(recursion_factorial(1))