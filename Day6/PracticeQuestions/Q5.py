#Date: 20/6/2024
#Author: Muhammad Muzammil

#Given a list of words, find the words with the maximum length and it's length.

lst = ['Day', 'six', 'Python', 'Code', 'challenge']

max_length = 0
max_word = ""
for word in lst:
    if len(word)>max_length:
        max_length = len(word)
        max_word = word

print(max_word)
print(max_length)
    