#Date: 21/6/2024
#Author: Muhammad Muzammil

#Write a Python program that counts the number of occurences of each character in a given string using a dictionary.

str = "My name is Muhammad Muzammil"

occurences = {}


for char in set(str):                       #Using set to ignore duplicate
    count = str.count(char)                 #for counting the character
    occurences.update({char : count})       #adding each character with count value in dictionary


#Just for printing
for x in occurences.items():
    print(x)