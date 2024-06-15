#Date: 14/6/2024
#Author: Muhammad Muzammil

#Create a Python function to check if a given string is a palindrome.
#A string is said to be palindrome if it remains the same on reading from both ends
#“madam”, “racecar”

def palindrome(str):
    reverse = "".join(reversed(str))
    if str == reverse:
        print(f"{str} is a palindrome string")
    else:
        print(f"{str} is not a palindrome string")

palindrome("banana")
palindrome("madam")
