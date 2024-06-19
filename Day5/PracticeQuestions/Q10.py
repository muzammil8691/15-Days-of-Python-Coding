#Date: 19/6/2024
#Author: Muhammad Muzammil

#Implement a program that takes a sentence and a word as input and check if the word is present in the sentence.

def word_presence_checker(sentence, word):
    sentence = sentence.lower()
    sentence = sentence.split()
    word = word.lower()

    if word in sentence:
        print("Found it")
    else:
        print("Not Found")


sentence = "Looking for a Scholarship to move Abroad"
word = "scholarship"

word_presence_checker(sentence, word)
