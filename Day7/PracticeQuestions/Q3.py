#Date: 21/6/2024
#Author: Muhammad Muzammil

#Implement a function that removes a key-value pair from a dictionary

def remove_pair(dict):
    dict.popitem()          #Removes the last pair 
    #dict.pop("Age")        #Removes the pair using key
    #del dict["Gender"]     #Removes the pair using key
    print(dict)


dict = {"Name": "Muzammil", "Gender": "Male", "Age": 24}

remove_pair(dict)