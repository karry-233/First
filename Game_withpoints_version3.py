#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 00:57:38 2018

@author: karry
"""


"""From 16 letters make words -Binary Search (second version)"""


from itertools import chain, combinations   
from more_itertools import unique_everseen


def word_to_key(word):
    return ''.join(sorted(word.lower()))


#Create subsets 
def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(5,len(s)+1))


#Binary Search
def find_the_word(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    item = word_to_key(item)
    while first<=last and not found:
        midpoint = (first + last)//2	 
        if alist[midpoint] == item:
            found = True
        else:	            
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


#calculate points
#didn't separate 'u' and 'Qu' two cases 
def get_point(word):
    point = 1
    for letter in word:
        if letter in 'abdeginorstu':
            point += 1 
        elif letter in 'cfhlmpvwy':
            point += 2
        elif letter in 'jkqxz':
            point += 3
    point = point ** 2
    return point



def get_anagrams(word):
    a = list(map(''.join, subsets(word)))
    b = list(unique_everseen(a))
    #to delete the duplicated items and keep the order
    for eachss in b:
        eachss = word_to_key(eachss)
        if find_the_word(word_list_key,eachss) == True:
            anagrams = word_list[eachss]
            print(anagrams,get_point(eachss))
        else:
            continue


#Create word list (hashtable)
words = open('dict.txt')
word_list = {}
for line in words:
    key = word_to_key(line.strip())
    if key in word_list:
        word_list[key].append(line.strip().lower())
    else:
        word_list[key] = [line.strip().lower()]
words.close()
word_list_key = sorted(word_list.keys())


get_anagrams(word=input('16 letters:'))
