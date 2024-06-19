#Date: 19/6/2024
#Author: Muhammad Muzammil

#Write a function to remove all duplicates characters from a given string.

def remove_duplicates(str):
    new_str = ""
    for char in str.lower():
        if char not in new_str:
            new_str += char
    
    print(new_str)

str = 'Muzammil'    
remove_duplicates(str)
