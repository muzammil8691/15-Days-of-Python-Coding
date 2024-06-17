#Date: 16/6/2024
#Author: Muhammad Muzammil

#Given a list of words, count the number of words with more than five characters.


def counter(word_lst):
    count = 0
    for word in word_lst:
        if len(word) > 5:
            count += 1
    return count


word_lst = ['15','Days','of','Python','Coding','Practice','Challenge','by','Muzammil']

print(f"{counter(word_lst)} words have more than five characters")