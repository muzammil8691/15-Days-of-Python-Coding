#Date: 19/6/2024
#Author: Muhammad Muzammil

#Write a function to count the number of vowels in a given string.
#The task has the same question repeated, so I'm just making the code better than the previous version.

def vowels_counter(str):
    count = 0
    for i in str:
        i =  i.lower()
        if i in ['a','e','i','o','u']:
            count+=1
    print(f"{count} vowels found.")


vowels_counter("This Is Day 5 Task")