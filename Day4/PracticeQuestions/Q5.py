#Date: 18/6/2024
#Author: Muhammad Muzammil

#write a function to check if a number is even or odd and return "Even" or "Odd" accordingly.

def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

print(even_odd(20))
print(even_odd(13))
print(even_odd(0))


