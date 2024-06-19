#Date: 19/6/2024
#Author: Muhammad Muzammil

#Write a Python program to find the length of the longest word in a sentence.

def longest_words(sentence):
    sentence = sentence.split() #Splits the string into list containing each word

    length = 0
    for word in sentence:
        if len(word) > length:
            length = len(word)
    
    print(f"Length of longest word is {length}")


sentence= "Why there is so many repeated questions in this task."
longest_words(sentence)
