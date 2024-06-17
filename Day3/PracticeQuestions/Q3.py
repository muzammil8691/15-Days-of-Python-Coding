#Date: 16/6/2024
#Author: Muhammad Muzammil

#Write a Pythopon program to check if a given number is a prime number.


def prime_number(number):
    if number <= 1:
        print(False)
        return

    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    print(prime)


prime_number(7)
prime_number(6)