#Date: 20/6/2024
#Author: Muhammad Muzammil

#Implement a function that takes two lists and returns their union(all unique elements from both lists)

def union(lst1, lst2):
    for element in lst1:
        if element not in unique_lst:
            unique_lst.append(element)

    for element in lst2:
        if element not in unique_lst:
            unique_lst.append(element)

    print(unique_lst)

lst1 = [1,6,7,4,5,7,4]
lst2 = [0,7,4,2,1,8,9]

unique_lst = []

union(lst1, lst2)