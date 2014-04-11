#!/usr/bin/env python

import sys

f = open(sys.argv[1], 'r')
data = f.read().split("\n")

#Ignore first line (number specification)
data = data[1:]

#Take care of potential trailing newline
while data[-1] == '':
    data = data[:-1]

for i, line in enumerate(data):
    temp = line.split(" ")
    temp.reverse()
    print ("Case #%d: " + " ".join(temp)) % (i+1)


