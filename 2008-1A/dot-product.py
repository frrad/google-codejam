#!/usr/bin/env python
import sys

#############
##Functions##
#############


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
#for trial in [0]:
for trial in range(trials):
    lgth = int(data[trial*3 + 1])
    v1 = map(int, data[trial*3 + 2].split(" "))
    v2 = map(int, data[trial*3 + 3].split(" "))

    print "Case #%d:" % (trial +1),
    v1.sort()
    v1.reverse()
    v2.sort()

    
    print sum(map(lambda a: a[0]*a[1], zip(v1, v2)))

