#Date: 15/6/2024
#Author: Muhammad Muzammil

#given a list of names, concatenate them into a single string seperated by spaces

def concat(lst):
    new_str = ""
    for i in lst:
        new_str += i + " "
    return new_str


names = ['Muzammil', 'Modasser', 'Yaseen']

print(concat(names))