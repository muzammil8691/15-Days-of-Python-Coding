#Date: 21/6/2024
#Author: Muhammad Muzammil

#Create a program that checks if two sets have any elements in common

set_1 = {2,4,6,8}
set_2 = {1,2,3,4,5,6,7,8}

#Method 1 ny for loop
for i in set_1:
    if i in set_2:
        print(i, end=",")

print()        

#Method 2 by built-in function

print(set(set_1).intersection(set_2))