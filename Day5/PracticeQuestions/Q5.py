#Date: 19/6/2024
#Author: Muhammad Muzammil

#Given a string, write a function to remove all vowels from it and return the modified string.

def vowel_eater(str):
    result=''
    for i in str:
        if i.lower() in ['a','e','i','o','u']:
            continue
        else:
            result += i
    print(result)

vowel_eater("Muzammil")
