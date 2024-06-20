#Date: 20/6/2024
#Author: Muhammad Muzammil

#Given a list of names, remove all duplicate names and print the unique names.

lst = ['Muzammil', 'Modasser', 'Ahmed', 'Yaseen', 'Muzammil', "Ali", "Yaseen"]
unique_names = []

for name in lst:
    if lst.count(name) > 1:
        continue
    else:
        unique_names.append(name)

print(unique_names)