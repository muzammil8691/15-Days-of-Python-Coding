#Date: 16/6/2024
#Author: Muhammad Muzammil

#Given a list of integers, find all the even numbers and store them in a new list.

def even_numbers(integers):
    
    new_list = []
    for i in integers:
        if i % 2 == 0:
            new_list.append(i)
    
    print(new_list)


integers = [1,4,3,5,6,8,334,23,12,9,0,5,6]
even_numbers(integers)