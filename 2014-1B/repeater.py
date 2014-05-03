#!/usr/bin/env python
import sys

#############
##Functions##
#############

def compress(x):
    stack = list()
    for letter in x:
        if len(stack) > 0 and stack[len(stack)-1][0] == letter:
            stack[len(stack)-1][1] += 1
        else:
            stack.append([letter, 1])
    return stack


def compute(stack):
    start = min(stack)
    stop = max(stack)
    winner = 999999999999999999
    for val in range(start, stop+1):
        count = 0
        for test in stack:
            count += abs(val - test)

        if count < winner: winner = count
    return winner


##############
##File Input##
##############
path = 'input.in'
if len(sys.argv)>1: path = sys.argv[1]

try:
    f = open(path, 'r')
except:
    quit("Error opening file: %s" % path)

data = f.read().splitlines()
f.close()

#Trim extra data from end of file
while data[-1] == '':
    data = data[:-1]
while data[0] == '':
    data = data[1:]

trials = int(data[0])

########
##Main##
########
data = data[1:]
trial = 0
#while trial == 0:
while len(data) > 0:
    spec = map(int, data[0].split(" "))
    specl = spec[0]
    x = data[1:specl + 1]
    data = data[specl + 1:]
    trial += 1

    words = int(spec[0])

    print "Case #%d: " %trial,
#    print "there are", words, "words"
 #   print "x = ",x
    info = map( compress, x)
#    print info
    standard =[]
    for rep in info:
        cp = ""
        for let in rep:
            cp += let[0]
        standard.append(cp)

    flag = False
    for word in standard:
        if word != standard[0]:
            flag = True
            print "Fegla Won"
            break
            
    if flag: continue

    tasty = 0
    


    for j in xrange(len(info[0])):
        tatertots = []
        for i in xrange(words):
            tatertots.append( info[i][j][1])
            
        tasty += compute(tatertots)
#        print tatertots, compute(tatertots)

    print tasty

