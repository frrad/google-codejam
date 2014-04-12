#!/usr/bin/env python
import sys

lookup = dict({
    " ": ("0", 1),
    "a": ("2", 1),
    "b": ("2", 2),
    "c": ("2", 3),
    "d": ("3", 1),
    "e": ("3", 2),
    "f": ("3", 3),
    "g": ("4", 1),
    "h": ("4", 2),
    "i": ("4", 4),
    "j": ("5", 1),
    "k": ("5", 2),
    "l": ("5", 3),
    "m": ("6", 1),
    "n": ("6", 2),
    "o": ("6", 3),
    "p": ("7", 1),
    "q": ("7", 2),
    "r": ("7", 3),
    "s": ("7", 4),
    "t": ("8", 1),
    "u": ("8", 2),
    "v": ("8", 3),
    "w": ("9", 1),
    "x": ("9", 2),
    "y": ("9", 3),
    "z": ("9", 4)
})

def type(input):
    output = ""
    for letter in input:
        if letter in lookup:
            if len(output) > 0 and lookup[letter][0] == output[-1]: output += " "
            output += lookup[letter][0] * lookup[letter][1]
        else:
            print "Can't find %s in loookup table" % letter

    return output



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
for trial in range(trials):
    line = str(data[trial*1 + 1])
    print "Case #%d: %s" % ((trial +1), type(line))


