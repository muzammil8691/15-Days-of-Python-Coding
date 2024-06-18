#Date: 18/6/2024
#Author: Muhammad Muzammil

#Write  a python function to check if a given string is a palindrome.

def palindrome(str):
    
    str = str.lower()
    if str == "".join(reversed(str)):
        print("Palindrome String")
    else:
        print("Not a Palindrome String")
        

palindrome("Chair")
palindrome("Civic")
palindrome("level")
