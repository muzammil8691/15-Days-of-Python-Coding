#Date: 19/6/2024
#Author: Muhammad Muzammil

#Given a list of names, count the number of names that start with a vowel.
def vowel_names(lst):
    count = 0

    for name in lst:
        name = name.lower()
        if name[0] in ['a','e','i','o','u']:
            count += 1
        
    print(f"{count} Names that starts with a Vowel")
lst = ['Muzammil','Ahmed','Imran','Yaseen','Khan']
vowel_names(lst)


