#Date: 16/6/2024
#Author: Muhammad Muzammil

#Create a loop that prints the first 10 even numbers.

#Method 1
print("---------------Method 1---------------")
for i in range(1,11):
    print(i*2)

#Method 2
print("---------------Method 2---------------")  
for i in range(2, 21, 2):
    print(i)

#Method 3
print("---------------Method 3---------------")
count = 0
while count < 10:
    count += 1
    print(count*2)
