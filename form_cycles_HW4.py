#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
input a word to find all the cycles it can form within n times
(using the link within n times, to find out all the ways to get back to the original word)
"""


import networkx as nx 


def build_graph():
    graph = nx.DiGraph()
    word_index = {}
    
    
    #add nodes to graph
    Indexs=open("pages.txt","r")
    for line in Indexs:
        Index_wikiWord = line.split()
        graph.add_node(Index_wikiWord[0])  
        word_index[Index_wikiWord[1]] = Index_wikiWord[0]
        # node is the index, not word
        # word_index = {"word":"index"}
    Indexs.close()
    
    #add edges to graph
    Links=open("links.txt","r")
    for line in Links:
        link = line.split()
        graph.add_edge(link[0],link[1])
    Links.close()
    
    return graph, word_index


# Confirm inputword exists in wikipedia and return the index of the inputword
def inputword_search(inputword):
    try:    
        index_of_inputword = word_index.get(inputword)
        print(inputword, "exists in wikipedia.")
        return index_of_inputword
    except:
        print(inputword, "is not in wikipedia.")
        print("Please try again.")
        exit(0)
    
    
def form_cycles(inputword,n):
    index_of_inputword = inputword_search(inputword)
    cycles = list(nx.all_simple_paths(graph,index_of_inputword,index_of_inputword,int(n))) 
    # find all the cycles that includes less than n nodes 
    if cycles == []:
        print("No cycle is found.")
    else:
        for cycle in cycles:
            print("Here is the cycle")
            for node in cycle:
                for word, index in word_index.items():   
                    if index == node:
                        print(word, "->")
            print("-------------------")
                   
    
graph, word_index = build_graph()
inputword = input("Please enter a word:")
n = input("Please decide the maximum size of cycles:")
form_cycles(inputword,n)
# n = 3,4,5...
