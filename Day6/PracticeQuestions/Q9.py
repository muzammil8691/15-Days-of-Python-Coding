#Date: 20/6/2024
#Author: Muhammad Muzammil

#Write a program that checks if a  given list is sorted in ascending order

lst = [2,3,4,5]

new_lst = lst[:]
new_lst.sort()

if lst == new_lst:
    print("Given list is in Ascending Order")

else:
    print("Given list is not in Ascending Order")