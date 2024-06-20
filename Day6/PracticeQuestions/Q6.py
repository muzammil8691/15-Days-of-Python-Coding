#Date: 20/6/2024
#Author: Muhammad Muzammil

#Write a Python program to count the occurences of each element in a given list.


lst = [1,6,4,5,2,3,1,8,7,6,8,5]
counted = []

for i in lst:
   if i in counted:     #This statement skips the already counted element
      continue
   
   x = lst.count(i)     #This statement counts the occurences
   print(f"{i} is found {x} times")

   counted.append(i)    #This statement appends the element which is counted in counted list


