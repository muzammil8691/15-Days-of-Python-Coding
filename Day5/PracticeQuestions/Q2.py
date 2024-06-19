#Date: 19/6/2024
#Author: Muhammad Muzammil

#Create a function to reverse a given string.

#Method 1
print("-----------------Method 1-----------------")
def reverse_str2(str):
    x = "".join(reversed(str))
    print(x)
reverse_str2("Monty")


#Method 2
print("-----------------Method 2-----------------")
def reverse_str(str):
        print(str[::-1], end="")


reverse_str("Python")
        
