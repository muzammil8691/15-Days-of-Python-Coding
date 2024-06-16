#Date: 15/6/2024
#Author: Muhammad Muzammil

#Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)
#A pangram is a sentence containing every letter in the English Alphabet.

def pangram(str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in alphabet:
        pangram = False

        if i in str:
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