#Date: 21/6/2024
#Author: Muhammad Muzammil

#Write a program that finds the average value of all the elements in the list of dictionaries.

dict_list = [{9,7,8}, {9,6,9}, {8,7,6}]
x = 0
y = 0
for dict in dict_list:
    x += sum(dict)
    y += len(dict)

avg = x/y
print(avg)