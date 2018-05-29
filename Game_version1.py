#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:53:28 2018

@author: karry
"""

def word_to_key(word):
    return ''.join(sorted(word.lower()))


def subsets():
    """L = input('16 letters:')  -String"""
    subset = []
    L = word_to_key(word)
    for i in range(len(L)):
        for j in range(i,len(L)):
            subset.append(L[i:j + 1])
    return subset


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
    for eachss in subsets():
        if eachss in build_word_list():
            anagrams = build_word_list()[eachss]
            for word in anagrams:
                print(word)
        else:
            continue
            #print('No anagrams')

word = input('16 letters:') 
get_anagrams()


