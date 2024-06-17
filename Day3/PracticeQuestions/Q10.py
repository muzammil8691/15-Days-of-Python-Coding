#Date: 16/6/2024
#Author: Muhammad Muzammil

#Calculate the sum of digits of a given number


def sum_of_digits(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    print(sum)


sum_of_digits(1234)
sum_of_digits(935)