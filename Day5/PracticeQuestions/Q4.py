#Date: 19/6/2024
#Author: Muhammad Muzammil

#Implement a function that checks if a given string is a pangram(contains all letters of the alphabets)
#This Question is also repeated so I am just writing a better code than previous one.


def pangram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet) #To convert this string's each alphabet into character in list.

    for i in alphabet:
        pangram = False

        if i in str.lower():
            pangram = True
            continue
        else:
            pangram = False
            break
    
    return pangram
    
    

result = pangram("The quick brown fox jumps over the lazy dog")

if result == True:
    print("Given String is a Pangram")

elif result == False:
    print("Given String is not a Pangram")
    