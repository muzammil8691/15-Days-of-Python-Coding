#Date: 14/6/2024
#Author: Muhammad Muzammil

#Given a list of integers, find the sum of all positive numbers.

def sum(lst):
    sum= 0
    for i in lst:
        if i > 0:
            sum += i
    
    return sum


integers = [2,5,-2,8,-10]
print(sum(integers))
