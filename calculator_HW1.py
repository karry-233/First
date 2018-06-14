#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:10:39 2018

@author: karry
"""


"""
calculator with plus, minus, multiply and divide function
"""


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
                print('Invalid syntax')
        index += 1
    return answer


def test(line, expectedAnswer):
    tokens = Newtokens(tokenize(line))
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)


# Add more tests to this function :)
def runTest():
    print "==== Test started! ===="
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    test("1.5*4+3-2/0.5",5)
    test("4.0/4*3.5-2",1.5)
    print "==== Test finished! ====\n"

runTest()

while True:
    print '> '
    line = raw_input()
    tokens = Newtokens(tokenize(line))
    answer = evaluate(tokens)
    print "answer = %f\n" % answer