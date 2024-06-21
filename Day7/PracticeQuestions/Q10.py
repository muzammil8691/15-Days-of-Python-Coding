#Date: 21/6/2024
#Author: Muhammad Muzammil

#Implement a function that takes a list of strings and returns a set of unique characters present in all strings.


lst = ["Day", "Seven", "of", "Python", "Coding", "Challenge"]

def unique_(lst):
    x = set()
    for str in lst:
        x.update(str.lower())

    return x

print(unique_(lst))
