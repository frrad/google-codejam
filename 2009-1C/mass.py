#!/usr/bin/env python
import sys, math

#############
##Functions##
#############

def com(t, flies):
    COM = [0.0 for i in range(3)]
    for fly in flies:
        pos = [float(fly[i]) + t*float(fly[3+i]) for i in range(3)]
        for i in range(3):
            COM[i] += pos[i]/len(flies)
    return COM

def dist(a,b):
    return math.sqrt(sum([a[i]**2 - b[i]**2 for i in range(3)]))

def minimize(fly):
    x = map(float, fly[:3])
    v = map(float, fly[3:])

    a = v[0]**2 + v[1]**2 + v[2]**2
    b = 2*v[0]*x[0] + 2*v[1]*x[1] + 2*v[2]*x[2]
    c = x[0]**2 + x[1]**2 + x[2]**2
    
    if a==0 and b==0: return 0

    return (-1*b) / (2*a)

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

while len(data) > 0:
    spec = map(int, data[0].split(" "))
    specl = spec[0]
    x = data[1:specl + 1]
    data = data[specl + 1:]
    trial += 1

    print "Case #%d: " %trial,
    flies = [map(int, line.split(" ")) for line in x]

    t = max(minimize(map(sum,zip(*flies))) , 0)

    print "%.8f %.8f" % (dist(com(t,flies), [0,0,0]), t)
