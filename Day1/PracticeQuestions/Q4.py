#Date: 14/6/2024
#Author: Muhammad Muzammil

#Given a list of numbers, find the maximum and minimum values.

lst = [13,45,6,34,9,15]

print("-----------------------Built-in Method-----------------------")

print(f"Maximum number from list is: {max(lst)}") #Using built-in max function
print(f"Minimum number from list is: {min(lst)}") #Using built-in min function

print("-----------------------Manual Method-----------------------")
#Manually finding maximum
highest = -99999999999    
for i in lst:
    if i > highest:
        highest = i
print(f"Highest value is: {highest}")


#Manually finding minimum
lowest = +99999999999
for i in lst:
    if i < lowest:
        lowest = i
print(f"Lowest value is: {lowest}")
