#Date: 16/6/2024
#Author: Muhammad Muzammil

#Create a loop that prints all prine numbers between 1 and 50

def prime_number(number):
    #This function checks if the number is prime or not #DocString
    if number <= 1:
        return False

    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    return prime

#Loop for 1 to 50
for i in range(1,50):
    result = prime_number(i)
    if result == True:
        print(i)