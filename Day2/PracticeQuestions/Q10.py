#Date: 15/6/2024
#Author: Muhammad Muzammil

#Write a program to check if a number is prime.
#For a number to be classified as a prime number, it should have exactly two factors.

def prime_nmbr_checker(number):
    decision = True

    if number == 1:
        decision = False
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:
                decision = False
                break
    return decision

flag =  prime_nmbr_checker(4)

if flag == False:
    print("Number is not Prime")
else:
    print("Prime Number")