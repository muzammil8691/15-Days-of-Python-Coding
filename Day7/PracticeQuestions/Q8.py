#Date: 21/6/2024
#Author: Muhammad Muzammil

#Create a function that takes a list of dictionaries and sort them based on a specified key
dict_list = [
    {'name': 'Muzammil', 'age': 30, 'score': 85},
    {'name': 'Yaseen', 'age': 25, 'score': 90},
    {'name': 'Ahmed', 'age': 35, 'score': 80}
]


def sorting(dict_list, key):
    sorted_dict = sorted(dict_list, key=lambda dict: dict[key])
    print(sorted_dict)


key = "name"
sorting(dict_list, key)
