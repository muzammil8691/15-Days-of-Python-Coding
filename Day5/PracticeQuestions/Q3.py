#Date: 19/6/2024
#Author: Muhammad Muzammil

#Write a program that takes a sentence as input and counts the number of words in it.

#Method 1
print("-----------------Method 1-----------------")

def words_counter(sentence):
    count = 1
    sentence = sentence.strip()
    for i in sentence:
        if i == " ":
            count += 1
    print(f" {count} words found in given string.")

words_counter("This task is also repeated.  ")


#Method 2
print("-----------------Method 2-----------------")

def words_counter2(sentence):
    words = sentence.count(" ") + 1
    print(f" {words} words found in given string.")

x = "My name is Muzammil. I am a practicing Python."
words_counter2(x)


#Method 3
print("-----------------Method 3-----------------")

def words_counter3(sentence):
    words = sentence.split()
    print(f" {len(words)} words found in given string.")

x = "Graduated from Hazara University Mansehra KPK"
words_counter3(x)
