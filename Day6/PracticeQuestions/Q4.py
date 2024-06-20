#Date: 20/6/2024
#Author: Muhammad Muzammil

#Create a program that finds the common elements between two lists and stores them in new list.

lst_1 = [2,3,5,6,8,9]
lst_2 = [1,2,4,5,7,8]
new_lst = []

for n in lst_1:
    if n in lst_2:
        new_lst.append(n)

print(new_lst)