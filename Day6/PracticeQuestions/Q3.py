#Date: 20/6/2024
#Author: Muhammad Muzammil

#Implement a function that takes a list of numbers and returns a new list with the squared values.

def square(lst):
    new_lst = []
    for n in lst:
        new_lst.append(n ** 2)

    print(new_lst)

    
lst = [2,4,6,8]
square(lst)