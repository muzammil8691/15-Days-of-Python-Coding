#Date: 21/6/2024
#Author: Muhammad Muzammil

#Write a program that finds the most frequent element in a list.

lst = [9,7,5,5,6,4,2,5,6,9,1]

m_frq = max(set(lst), key= lst.count)
print(m_frq)
