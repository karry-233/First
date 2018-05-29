#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 23:18:03 2018

@author: karry
"""

"""Make a program that can find single word anagrams that use all the characters in a given string 
(e.g. “omnsotare” -> “astronomer”)"""

def word_to_key(word=input("Anagram letters: ")):
    return ''.join(sorted(word.lower()))

#creat a hashtable
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

def get_anagrams():
    key = word_to_key()
    if key in build_word_list():
        anagrams = build_word_list()[key]
        for word in anagrams:
            print(word)
    else:
        print('No anagrams')
 
get_anagrams()
