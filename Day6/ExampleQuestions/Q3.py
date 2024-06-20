#Date: 20/6/2024
#Author: Muhammad Muzammil

#Access elements in a tuple using inndexing

cars = ('Toyota', 'Honda', 'Kia', 'Suzuki', 'Mercedes', 'Audi', 'BMW')

print(cars[0])   #Expected Toyota
print(cars[-1])  #Expected BMW
print(cars[1:4]) #Expected Honda, Kia, Suzuki
print(cars[-1:-4:-1]) #Expected BMW, Audi, Mercedes