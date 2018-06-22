#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:48:52 2018

@author: karry
"""


"""calculator with plus, minus, multiply, divide and brackets function"""


import re


def readNumber(line, index):
    number = 0
    flag = 0
    keta = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + float(line[index])
            if flag == 1:
                keta *= 0.1
        index += 1
    token = {'type': 'NUMBER', 'number': number * keta}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def readDivide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '*':
            (token, index) = readMultiply(line, index)
        elif line[index] == '/':
            (token, index) = readDivide(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def Newtokens(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLY':
                result = tokens[index]['number'] * tokens[index-2]['number']
                token = {'type': 'NUMBER', 'number': result}
                tokens.insert(index+1, token)
                del tokens[index-2:index+1]
                index -= 2
            elif tokens[index - 1]['type'] == 'DIVIDE' and tokens[index]['number'] != 0:
                result = tokens[index-2]['number'] / tokens[index]['number']
                token = {'type': 'NUMBER', 'number': result}
                tokens.insert(index+1, token)
                del tokens[index-2:index+1]
                index -= 2
            elif tokens[index - 1]['type'] == 'DIVIDE' and tokens[index]['number'] == 0:
                print 'cannot be calculated'
                exit(1)
        index += 1
    return tokens

        
def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer
#Until here, all the same as homework2 
#calculate for +=*/


#use howework2's function to calculate the part inside a bracket and return the answer
def resolve_line_within_brackets(expr):
    tokens = Newtokens(tokenize(expr))
    answer = evaluate(tokens)
    return answer

#function to calculate the whole equation and return the final answer to the whole equation 
def general_calculate(line):
    inner_brackets_found = True
    while inner_brackets_found:    #loop until there is no brackets left in the equation 
        m = re.search('\([^\(\)]+\)', line)
        if m != None:
            #get the equation inside the bracket which should be calculated first 
            line_with_brackets = line[m.start():m.end()]
            subline= line_with_brackets[1:-1]
            answer = str(resolve_line_within_brackets(subline))    #calculate the part inside the bracket
            line = line.replace(line_with_brackets, answer)
            #put the answer back into the original equation and get a new equation 
        else:
            #in the case there is no brackets in the equation 
            inner_brackets_found = False    
            answer = resolve_line_within_brackets(line)
    return answer


def test(line, expectedAnswer):
    actualAnswer = general_calculate(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)

        
def runTest():
    print "==== Test started! ===="
    test("2.0*3", 6)
    test("1.2+2*3", 7.2)
    test("(3*(1+4)-9)*(5+(3*(2-1)))", 48)
    test("(1.0+2.1-3)*6+3", 3.6)
    test("2.0*(3/5.0+2)", 5.2)
    print "==== Test finished! ====\n"

runTest()


while True:
    print ">"
    line = raw_input()
    answer = general_calculate(line)
    print "answer = %f\n" % answer

