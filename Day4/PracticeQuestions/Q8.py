#Date: 18/6/2024
#Author: Muhammad Muzammil

#write  a function that takes two lists and return their intersection (common elements).

def intersection(lst1, lst2):
    common = []
    for element in lst1:
        if element in lst2:
            common.append(element)
    print(common)

lst1 = [1,6,8,4]
lst2 = [9,4,2,1]

intersection(lst1, lst2)