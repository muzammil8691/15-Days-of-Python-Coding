#Date: 18/6/2024
#Author: Muhammad Muzammil

#implement a function that reverses a given string.


#Method 1 #Built-in 
print("----------------Method 1----------------")

def reverse_string(str):
    x = "".join(reversed(str))
    print(x)

reverse_string("Reversing by Built-in Method")


#Method 2 #Manual
print("----------------Method 2----------------")

def reverse_string(str):
    x = -1
    for i in str:
        print(str[x], end="")
        x -= 1

reverse_string("Reversing by Manual Method")