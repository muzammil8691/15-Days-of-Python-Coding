#Date: 16/6/2024
#Author: Muhammad Muzammil

#write a program that calculates the factorial of a given number

def factorial(number):
    f=1
    for i in range(1, number):
        f = f * (i+1)
    return f
        


print(f"Factorial is {factorial(5)}")
print(f"Factorial is {factorial(0)}")
print(f"Factorial is {factorial(1)}")
print(f"Factorial is {factorial(9)}")


