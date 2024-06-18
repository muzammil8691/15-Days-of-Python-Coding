#Date: 18/6/2024
#Author: Muhammad Muzammil

#Given a list of numbers, create a function to find the sum of all positive numbers.

def sum_of_positive_numbers(numbers):
    
    sum = 0
    for i in numbers:
        if i > 0:
            sum += i
    print(sum)


lst = [30,-5,23,1,6,0,-9]
sum_of_positive_numbers(lst)