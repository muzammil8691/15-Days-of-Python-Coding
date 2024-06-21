#Date: 21/6/2024
#Author: Muhammad Muzammil

#Given two dictionaries, merge them into a single dictionary.

dict_1 = {"Name": "Muzammil", "Gender": "Male", "Age": 24}

dict_2 = {"Mail": "m.muzammil8691@gmail.com", "Education": "BS Software Engineering"}


dict_1.update(dict_2) #Dict_2 is merged into Dict_1
print(dict_1)

x = {**dict_1, **dict_2} # Both merged into another variable
print(x)
