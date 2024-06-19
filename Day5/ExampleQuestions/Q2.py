#Date: 19/6/2024
#Author: Muhammad Muzammil

#Write a function to count the number of vowels in a given string.

def vowels_counter(str):
    count = 0
    for i in str:
        if i in ['a','e','i','o','u']:
            count+=1
    print(f"{count} vowels found.")


vowels_counter("This is Day 5 Task")