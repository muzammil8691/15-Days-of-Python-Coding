#Date: 21/6/2024
#Author: Muhammad Muzammil

#Given a list of dictionaries, find the dictionary with the highest value for a specific key

dict_list = [
    {'name': 'Muzammil', 'age': 30, 'score': 85},
    {'name': 'Yaseen', 'age': 25, 'score': 90},
    {'name': 'Ahmed', 'age': 35, 'score': 80}
]

score = 0
max_dict = None

s_key = "score"             #The key to search for

for dict in dict_list:
    if dict[s_key] > score:
        score = dict[s_key]
        max_dict = dict


print(max_dict)