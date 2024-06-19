#Date: 19/6/2024
#Author: Muhammad Muzammil

#Given a list of words, concatenate them into a single string seperated by spaces.

#Method 1
print("-----------------Method 1-----------------")

def concat(lst):
    for i in lst:
        print(i, end=" ")

lst = ['Day','5','Practice','Question','1']
concat(lst)


#Method 2
print()
print("-----------------Method 2-----------------")

def concat(lst):
    for i in lst:
      x =  " ".join(lst)
    print(x)


lst = ['Day','5','Practice','Question','1']
concat(lst)