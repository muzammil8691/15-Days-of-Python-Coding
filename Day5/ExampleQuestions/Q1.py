#Date: 19/6/2024
#Author: Muhammad Muzammil

#Create a program that checks if a given string is a palindrome.

# function which return reverse of a string

def palindrome(s):
	return s == s[::-1]



ans = palindrome("level")

if ans:
	print("Palindrome")
else:
	print("Not a Palindrome")
