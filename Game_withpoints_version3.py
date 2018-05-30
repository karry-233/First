#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 00:57:38 2018

@author: karry
"""

def word_to_key(word):
    return ''.join(sorted(word.lower()))


#Create word list (hashtable)
def build_word_list(words='dict.txt'):
    words = open(words)
    word_list = {}
    for line in words:
        key = word_to_key(line.strip())
        if key in word_list:
            word_list[key].append(line.strip().lower())
        else:
            word_list[key] = [line.strip().lower()]
    words.close()
    return word_list  


#Create subsets
def subsets():
    """L = input('16 letters:')  -String"""
    subset = []
    L = word_to_key(word)
    for i in range(len(L)):
        for j in range(i,len(L)):
            subset.append(L[i:j + 1])
    return subset


#Binary Search
def find_the_word(alist, item):
    alist = sorted(alist)
    first = 0
    last = len(alist)-1
    found = False
	
    while first<=last and not found:
        midpoint = (first + last)//2	 
        if alist[midpoint] == word_to_key(item):
            found = True
        else:	            
            if word_to_key(item) < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
	
    return found


#calculate points
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


def get_anagrams():
    for eachss in subsets():
        if find_the_word(build_word_list(),eachss) == True:
            anagrams = build_word_list()[eachss]
            for word in anagrams:
                print(word,get_point(word))
        else:
            continue
            #print('No anagrams')

word = input('16 letters:')  

get_anagrams()

