#Date: 20/6/2024
#Author: Muhammad Muzammil

#Create a function that takes a list of strings and returns the list sorted by the length of strings.

def sorting_len(lst):
    lst.sort(key=len)
    return lst


lst = ['Day', 'six', 'of', 'Python', 'Coding', 'challenge']
print(sorting_len(lst))
