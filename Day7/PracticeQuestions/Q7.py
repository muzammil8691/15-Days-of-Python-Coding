#Date: 21/6/2024
#Author: Muhammad Muzammil

#Given two sets find the union, intersection, and difference between them.

set_1 = {1,2,4,5,6,7,8}
set_2 = {1,3,5,7,9,11}

print("---------------Union---------------")
x = set_1.union(set_2)    #Gives all elements in set_1 and set_2 ignoring duplicates
print(x)

print("---------------Intersection---------------")
y = set_1.intersection(set_2)
print(y)

print("---------------differences---------------")

z = set_1.symmetric_difference(set_2) #Elements of both sets not found in the other
#z = set_1.difference(set_2)          #Elements of set 1 not in set 2  
print(z)
