#Date: 19/6/2024
#Author: Muhammad Muzammil

#Create a function that a sentence as input and returns the sentence in reverse order.

def sentence_reverse(sentence):
    sentence = sentence.split()

    reversed_sentence = ' '.join(reversed(sentence))
    print(reversed_sentence)


sentence_reverse("coding doing am I and Eid It's")
