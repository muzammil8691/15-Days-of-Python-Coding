#Date: 18/6/2024
#Author: Muhammad Muzammil

#create a function that takes a list of strings and returns the list sorted alphabetically.

print('-----------------Case Sensitive Method-----------------')
def sorting(lst):
    #return sorted(lst) #Method 1
    lst.sort()          #Method 2
    return lst

lst = ['Dog', 'baby', 'Apple', 'Cat']
print(sorting(lst))



print('-----------------Case In-Sensitive Method-----------------')
def sorting(lst):
    # return sorted(lst, key=str.lower) #Method 1
    lst.sort(key = str.lower)          #Method 2
    return lst

lst = ['Dog', 'baby', 'Apple', 'Cat']
print(sorting(lst))
