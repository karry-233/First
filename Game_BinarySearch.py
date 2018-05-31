#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 19:36:16 2018

@author: karry
"""


"""From 16 letters make words -Binary Search (second version)"""


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
from itertools import chain, combinations    

def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s),5,-1))

#Binary Search
def find_the_word(alist,item):
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

from more_itertools import unique_everseen

def get_anagrams(word):
    a = list(map(''.join, subsets(word)))
    b = list(unique_everseen(a))
    for eachss in b:
        #print(eachss)
        if find_the_word(build_word_list(),eachss) == True:
            anagrams = build_word_list()[word_to_key(eachss)]
            print(anagrams)
        else:
            continue


get_anagrams(word=input('16 letters:'))

