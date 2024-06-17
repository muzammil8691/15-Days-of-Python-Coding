#Date: 16/6/2024
#Author: Muhammad Muzammil

#Given a list of names, print all names starting with the letter "A".

#Method 1
print("----------------Method 1----------------")
def print_names(lst):
    for i in lst:
        if i[0].lower() == 'a':
            print(i)


lst = ['Muzammil', 'Abdullah', 'Yaseen', "Ahmed"]
print_names(lst)




#Method 2
print("----------------Method 2----------------")
def print_names(lst):
    for i in lst:
        if i.startswith('A') or i.startswith('a'):
            print(i)

lst = ['Muzammil', 'Abdullah', 'Yaseen', "Ahmed"]
print_names(lst)
