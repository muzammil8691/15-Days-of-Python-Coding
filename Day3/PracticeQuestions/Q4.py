#Date: 16/6/2024
#Author: Muhammad Muzammil

#Q=Create a program that generates the Fibonacci sequence up to a given number of terms.
#the sequence of numbers in which each number in the sequence is equal to the sum of two numbers before it


def fibonacci(n):
    if n <= 0:
        return "Enter a positive value"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    lst = [0,1]
    for i in range(n - 2):
        lst.append(lst[-1] + lst[-2])
    
    return lst

sequence = fibonacci(8)
print(sequence)