#Date: 18/6/2024
#Author: Muhammad Muzammil

#create a function to check if a number is prime.

def check_prime(number):
    if number<=0:
        print("Enter a valid number")

    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True

print(check_prime(3))
print(check_prime(6))
print(check_prime(11))
print(check_prime(0))
