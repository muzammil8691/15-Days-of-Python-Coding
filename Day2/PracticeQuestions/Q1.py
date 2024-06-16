#Date: 15/6/2024
#Author: Muhammad Muzammil

#Given a list of numbers, find the sum and average

def sum(numbers):
    #this function calculates sum #DocString
    s = 0
    for i in numbers:
        s += i

    return s

def average(data):
    #this function calculates average #DocString
    avg = sum(lst)/len(data)

    return avg



lst = [1,2,3,4,5]

print(f"Sum of numbers is {sum(lst)}")

print(f"Average of numbers is {average(lst)}")
