#Date: 16/6/2024
#Author: Muhammad Muzammil

#Implement a program that finds the largest number in a list.


#Method 1 
print("---------------Method 1---------------")
def find_largest(numbers):
    print(max(numbers))

lst = [2,45,7,65,33,20]
find_largest(lst)


#Method 2
print("---------------Method 2---------------")
def find_largest(numbers):
    largest = -9999999
    for i in numbers:
        if i > largest:
            largest = i
    
    print(largest)

lst = [2,45,7,65,33,20]
find_largest(lst)
