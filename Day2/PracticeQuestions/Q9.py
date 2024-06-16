#Date: 15/6/2024
#Author: Muhammad Muzammil

#Create a function to count the number of vowels in a given string

def vowels_counter(string):
    count = 0
    for i in string:
        if i.lower() in ['a','e','i','o','u']:
            count += 1
    print(f"{count} vowels found in given string")


vowels_counter("hello my name is Muzammil")
vowels_counter("AeIoU")